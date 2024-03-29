from uuid import uuid4
from database import connect_to_mongodb, create_challenge_collection, get_collection
from Levenshtein import ratio
from flask import jsonify
from datetime import datetime, timedelta
from wtforms import Form, IntegerField, validators
from re import sub


MINIMUM_RATIO = 0.9


class CreateChallengeForm(Form):
    question_amount = IntegerField("SFX amount", [validators.DataRequired(), validators.NumberRange(min=10, max=30)])
    minimum_year = IntegerField("Minimum year", [validators.DataRequired(), validators.NumberRange(min=1998, max=2022)])


def collection_exists(uuid, db):
    list_of_collections = db.list_collection_names()
    return uuid in list_of_collections


def select_random_sounds(db, amount, min_year):
    sounds_collection = db
    pipe1 = [
        {"$match": {"game_year": {"$gte": min_year}}},
        {"$sample": {"size": amount}}
    ]
    sounds_list = list(sounds_collection.aggregate(pipe1))
    return sounds_list


def add_new_challenge(db, amount, min_year):
    challenge_uuid = str(uuid4())
    sounds = select_random_sounds(db, amount, min_year)
    db_challenges = connect_to_mongodb("Challenges")
    create_challenge_collection(challenge_uuid, db_challenges, sounds)
    return challenge_uuid


def add_deletion_date(uuid, db):
    deletion_dates_collection = get_collection(db, "Deletion dates")
    deletion_date = datetime.now() + timedelta(days=2)
    # noinspection PyUnusedLocal
    insertion_id = deletion_dates_collection.insert_one({"uuid": uuid, "deletion_date": deletion_date})


def extend_deletion_date(db, uuid):
    deletion_dates_collection = get_collection(db, "Deletion dates")
    new_deletion_date = datetime.now() + timedelta(days=2)
    # noinspection PyUnusedLocal
    update_id = deletion_dates_collection.update_one({"uuid": uuid}, {"$set": {"deletion_date": new_deletion_date}})


def get_audio_file_path(name_uuid, db):
    sounds_collection = get_collection(db, "Sounds")
    file_name = sounds_collection.find({"_id": {"$eq": name_uuid}})[0]["associated_file"]
    return file_name


def compare_answer_to_game_name_by_id(challenge_uuid, db, sfx_id, guess):
    challenge_collection = get_collection(db, challenge_uuid)
    sfx_status = challenge_collection.find({"_id": {"$eq": sfx_id}})[0]["status"]
    if sfx_status == "result_shown":
        return jsonify({"game_name": "Cheater"})
    game_name = challenge_collection.find({"_id": {"$eq": sfx_id}})[0]["game_name"]
    # sub('[^a-z0-9]+', '', game_name.lower())
    # sub('[^a-z0-9]+', '', guess.lower())
    if ratio(sub('[^a-z0-9]+', '', game_name.lower()), sub('[^a-z0-9]+', '', guess.lower())) >= MINIMUM_RATIO:
        challenge_collection.update_one({"_id": sfx_id}, {"$set": {"status": "correct_guess"}}, upsert=False)
        return jsonify({"sfx_id": sfx_id, "game_name": game_name, "status": "correct_guess"})
    else:
        challenge_collection.update_one({"_id": sfx_id}, {"$set": {"status": "incorrect_guess"}}, upsert=False)
        return jsonify({"sfx_id": sfx_id, "game_name": "False", "status": "incorrect_guess"})


def get_challenge_content(challenge_uuid, db):
    challenge_collection = get_collection(db, challenge_uuid)
    challenge_content = [{"challenge_uuid": challenge_uuid}]
    sfxs_contents = []
    for sfx in challenge_collection.aggregate([{"$project": {"status": 1, "game_name": {"$switch": {"branches": [{"case": {"$eq": ["$status", "correct_guess"]}, "then": "$game_name"}, {"case": {"$eq": ["$status", "incorrect_guess"]}, "then": ""}, {"case": {"$eq": ["$status", "result_shown"]}, "then": "$game_name"}], "default": ""}}}}]):
        sfxs_contents.append(sfx)
    challenge_content.append({"sfxs_contents": sfxs_contents})
    return challenge_content


def get_challenge_results_content(challenge_uuid, db):
    challenge_collection = get_collection(db, challenge_uuid)
    challenge_results_content = [{"challenge_uuid": challenge_uuid}]
    sfxs_contents = []
    for sfx in challenge_collection.find({}, {"id": 1, "game_name": 1, "status": 1}):
        if sfx["status"] in ["no_guess", "incorrect_guess"]:
            challenge_collection.update_one({"_id": sfx["_id"]}, {"$set": {"status": "result_shown"}})
        sfxs_contents.append(sfx)
    challenge_results_content.append(sfxs_contents)
    return challenge_results_content


def delete_outdated_challenges(db_challenges, db_sfxchallenge):
    deletion_dates_collection = get_collection(db_sfxchallenge, "Deletion dates")
    for date in deletion_dates_collection.find({}, {"deletion_date": 1, "_id": 0, "uuid": 1}):
        if datetime.now() > date["deletion_date"]:
            db_challenges.drop_collection(date["uuid"])
            deletion_dates_collection.delete_one({"uuid": date["uuid"]})
    return '', 200

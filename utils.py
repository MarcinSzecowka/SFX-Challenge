from uuid import uuid4
from database import connect_to_mongodb, create_challenge_collection, get_collection
from Levenshtein import ratio
from flask import jsonify


MINIMUM_RATIO = 0.8


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


def create_new_challenge(db, amount, min_year):
    challenge_uuid = str(uuid4())
    sounds = select_random_sounds(db, amount, min_year)
    db_challenges = connect_to_mongodb("Challenges")
    create_challenge_collection(challenge_uuid, db_challenges, sounds)
    return challenge_uuid


def compare_answer_to_game_name_by_id(challenge_uuid, db, sfx_id, guess):
    challenge_collection = get_collection(db, challenge_uuid)
    game_name = challenge_collection.find({"_id": {"$eq": sfx_id}})[0]["game_name"]
    if ratio(game_name.lower(), guess.lower()) >= MINIMUM_RATIO:
        challenge_collection.update_one({"_id": sfx_id}, {"$set": {"status": "correct_guess"}}, upsert=False)
        return jsonify({"sfx_id": sfx_id, "game_name": game_name, "status": "correct_guess"})
    else:
        challenge_collection.update_one({"_id": sfx_id}, {"$set": {"status": "incorrect_guess"}}, upsert=False)
        return jsonify({"sfx_id": sfx_id, "game_name": "False", "status": "incorrect_guess"})


def get_challenge_content(challenge_uuid, db):
    challenge_collection = get_collection(db, challenge_uuid)
    challenge_content = [{"challenge_uuid": challenge_uuid}]
    sfxs_contents = []
    for sfx in challenge_collection.aggregate([{"$project": {"status": 1, "game_name": {"$cond": {"if": {"$eq": ["$status", "correct_guess"]}, "then": "$game_name", "else": ""}}}}]):  # ,"else": "$$REMOVE" could also be used, but leaving it in and making it empty makes it easier to handle by the frontend (I would have to make an if statement in jinja which is arguably more complicated to implement)
        sfxs_contents.append(sfx)
    challenge_content.append({"sfxs_contents": sfxs_contents})
    return challenge_content


def get_challenge_results_content(challenge_uuid, db):
    challenge_collection = get_collection(db, challenge_uuid)
    challenge_results_content = [{"challenge_uuid": challenge_uuid}]
    sfxs_contents = []
    for sfx in challenge_collection.find({}, {"id": 1, "game_name": 1, "status": 1}):
        sfxs_contents.append(sfx)
    challenge_results_content.append(sfxs_contents)
    return challenge_results_content

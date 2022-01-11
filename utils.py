from uuid import uuid4
from database import connect_to_mongodb, create_challenge_collection, get_collection
from Levenshtein import ratio


MINIMUM_RATIO = 0.8


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
        challenge_collection.update_one({"_id": sfx_id}, {"$set": {"status": 1}}, upsert=False)
        return game_name
    else:
        challenge_collection.update_one({"_id": sfx_id}, {"$set": {"status": 2}}, upsert=False)
        return "False"


def get_challenge_content(challenge_uuid, db):
    # todo use flask.send_file() to send a file in the future
    challenge_collection = get_collection(db, challenge_uuid)
    challenge_content = [{"challenge_uuid": challenge_uuid}]
    sfxs_contents = []
    for sfx in challenge_collection.find({}, {"id": 1, "associated_file": 1}):
        sfxs_contents.append(sfx)
    challenge_content.append({"sfxs_contents": sfxs_contents})
    return challenge_content


def get_challenge_results_content(challenge_uuid, db):
    # todo use flask.send_file() to send a file in the future
    challenge_collection = get_collection(db, challenge_uuid)
    challenge_results_content = [{"challenge_uuid": challenge_uuid}]
    sfxs_contents = []
    for sfx in challenge_collection.find({}, {"id": 1, "game_name": 1, "associated_file": 1, "status": 1}):
        sfxs_contents.append(sfx)
    challenge_results_content.append(sfxs_contents)
    return challenge_results_content

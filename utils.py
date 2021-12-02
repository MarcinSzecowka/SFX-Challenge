from uuid import uuid4
from database import connect_to_mongodb, create_challenge_collection, get_collection


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
    # todo change below code so that it uses levenshtein
    if game_name == guess:
        return game_name
    else:
        return "False"

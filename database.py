import pymongo


def connect_to_mongodb(database):
    username = "root"
    password = "rootpassword"
    client = pymongo.MongoClient("mongodb://localhost:27017/", username=username, password=password)
    database = client[f"{database}"]
    return database


def get_collection(database):
    collection = database["test"]
    return collection


def create_challenge_collection(challenge_uuid, db_challenges, sounds):
    new_challenge_collection = db_challenges[challenge_uuid]
    insert_into_col = new_challenge_collection.insert_one(sounds)

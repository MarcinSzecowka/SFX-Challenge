import os

import pymongo


def connect_to_mongodb(database):
    # username = "root"
    # password = "rootpassword"
    # client = pymongo.MongoClient("mongodb://localhost:27017/", username=username, password=password)
    client = pymongo.MongoClient(f"{os.getenv('MONGODB_URI')}")
    database = client[f"{database}"]
    return database


def get_collection(database, name):
    collection = database[name]
    return collection


def create_challenge_collection(challenge_uuid, db_challenges, sounds):
    new_challenge_collection = db_challenges[challenge_uuid]
    # noinspection PyUnusedLocal
    insert_into_col_id = new_challenge_collection.insert_many(sounds)

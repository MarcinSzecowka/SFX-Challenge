import os

import pymongo


def connect_to_mongodb(database):
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


def update_sounds_collection(collection, sounds_data):
    collection.delete_many({})
    collection.insert_many(sounds_data)

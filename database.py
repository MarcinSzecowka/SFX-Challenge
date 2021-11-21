import pymongo


def connect_to_mongodb():
    username = "root"
    password = "rootpassword"
    client = pymongo.MongoClient("mongodb://localhost:27017/", username=username, password=password)
    database = client["SFXChallenge"]
    return database


def get_collection(database):
    collection = database["test"]
    return collection

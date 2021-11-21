import flask

from database import connect_to_mongodb, get_collection

db = connect_to_mongodb()
my_collection = get_collection(db)

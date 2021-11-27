import pymongo
from flask import Flask, request, jsonify, url_for, redirect
from database import connect_to_mongodb, get_collection
from utils import create_new_challenge

db = connect_to_mongodb()
my_collection = get_collection(db)

app = Flask(__name__)


@app.route("/")
def return_homepage():
    # Separate buttons for each game mode like: modern/classics/all
    return "<p>Homepage</p>"


@app.route("/modern", methods=["GET", "POST"])
def create_new_modern_challenge():
    if request.method == "GET":
        return "<p>Hello, World!</p>"
    if request.method == "POST":
        amount = request.form.get("amount")
        min_year = request.form.get("year")
        new_uuid = create_new_challenge(amount, min_year)
        return redirect(url_for('challenge', uuid=new_uuid), code=302)


@app.route("/<uuid>")
def challenge(uuid):
    uuid1 = uuid
    return f"<p>challenge page 123 uuid:{uuid1}</p>"


if __name__ == '__main__':
    app.run(debug=True)

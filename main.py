from flask import Flask, request, url_for, redirect, jsonify
from database import connect_to_mongodb, get_collection
from utils import create_new_challenge, compare_answer_to_game_name_by_id, get_challenge_content, \
    get_challenge_results_content
from sounds import populate_sounds_collection

db_sfxchallenge = connect_to_mongodb("SFXChallenge")
db_challenges = connect_to_mongodb("Challenges")

my_sfxchallenge_collection = get_collection(db_sfxchallenge, "test")

sounds_collection = get_collection(db_sfxchallenge, "Sounds")
sounds_collection.drop()
sounds_collection = get_collection(db_sfxchallenge, "Sounds")
populate_sounds_collection(sounds_collection)

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
        amount = int(request.form.get("amount"))
        min_year = int(request.form.get("min_year"))
        new_uuid = create_new_challenge(sounds_collection, amount, min_year)
        return redirect(url_for('challenge', uuid=new_uuid), code=302)


@app.route("/<uuid>", methods=["GET", "POST"])
def challenge(uuid):
    if request.method == "GET":
        challenge_uuid = uuid
        challenge_content = get_challenge_content(challenge_uuid, db_challenges)
        return jsonify(challenge_content)
    if request.method == "POST":
        challenge_uuid = uuid
        sfx_id = str(request.form.get("sfx_id"))
        guess = str(request.form.get("guess"))
        return compare_answer_to_game_name_by_id(challenge_uuid, db_challenges, sfx_id, guess)


@app.route("/<uuid>/results", methods=["GET"])
def challenge_results(uuid):
    if request.method == "GET":
        challenge_uuid = uuid
        challenge_results_content = get_challenge_results_content(challenge_uuid, db_challenges)
        return jsonify(challenge_results_content)


# todo add a timestamp to all newly created challenges and remove them automatically after a few days
##############################
# todo add multiplayer option by utilizing websockets
##############################
# todo implement asynchronous requests so that the user can see challenge answers without being redirected to a new site


if __name__ == '__main__':
    app.run(debug=True)

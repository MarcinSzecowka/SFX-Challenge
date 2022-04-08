from flask import Flask, request, url_for, redirect, jsonify, render_template, send_file
from database import connect_to_mongodb, get_collection
from utils import create_new_challenge, compare_answer_to_game_name_by_id, get_challenge_content, \
    get_challenge_results_content, collection_exists
from sounds import populate_sounds_collection
from pathlib import Path
import os


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
    return redirect(url_for("create_new_modern_challenge"), code=301)


@app.route("/modern", methods=["GET", "POST"])
def create_new_modern_challenge():
    if request.method == "GET":
        return render_template("create_new_challenge.html")
    if request.method == "POST":
        amount = int(request.form.get("amount"))
        min_year = int(request.form.get("min_year"))
        new_uuid = create_new_challenge(sounds_collection, amount, min_year)
        return redirect(url_for('challenge', uuid=new_uuid), code=302)


@app.route("/challenge/<uuid>", methods=["GET", "POST"])
def challenge(uuid):
    if request.method == "GET":
        challenge_uuid = str(uuid)
        if collection_exists(challenge_uuid, db_challenges):
            challenge_content = get_challenge_content(challenge_uuid, db_challenges)
            return render_template("challenge.html", json_obj=challenge_content)
        else:
            return render_template("challenge_non_existent.html")
    if request.method == "POST":
        challenge_uuid = uuid
        sfx_id = str(request.form.get("sfx_id"))
        guess = str(request.form.get("guess"))
        return compare_answer_to_game_name_by_id(challenge_uuid, db_challenges, sfx_id, guess)


@app.route("/challenge/<uuid>/results", methods=["POST"])
def challenge_results(uuid):
    if request.method == "POST":
        challenge_uuid = str(uuid)
        challenge_results_content = get_challenge_results_content(challenge_uuid, db_challenges)
        return jsonify(challenge_results_content)
        # todo implement another endpoint in challenge.html that will send a request to this endpoint and receive
        #   challenge results as a response, then update the page accordingly


@app.route("/audio/<audio_file_name>")
def return_audio_file(audio_file_name):
    base_path = Path(__file__).parent
    audio_file_path = os.path.join(base_path, "audio", audio_file_name + ".mp3")
    return send_file(
        audio_file_path,
        mimetype="audio/mp3",
        as_attachment=False,)


@app.errorhandler(404)
def handle_error_404(e):
    return redirect(url_for("create_new_modern_challenge"), code=301)


# todo add a timestamp to all newly created challenges and remove them automatically after a few days
# todo refresh challenge deletion date when you revisit a challenge
##############################
# todo add multiplayer option by utilizing websockets
##############################


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, url_for, redirect, jsonify, render_template, send_file, send_from_directory
from database import connect_to_mongodb, get_collection
from utils import create_new_challenge, compare_answer_to_game_name_by_id, get_challenge_content, \
    get_challenge_results_content, collection_exists, add_deletion_date, delete_outdated_challenges, \
    extend_deletion_date
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
    return redirect(url_for("create_new_modern_challenge"), code=302)


@app.route("/create/modern", methods=["GET", "POST"])
def create_new_modern_challenge():
    if request.method == "GET":
        return render_template("create_new_challenge.html")
    if request.method == "POST":
        amount = int(request.form.get("question_amount"))
        min_year = int(request.form.get("min_year"))
        new_uuid = create_new_challenge(sounds_collection, amount, min_year)
        add_deletion_date(new_uuid, db_sfxchallenge)
        return redirect(url_for('challenge', challenge_uuid=new_uuid), code=302)


@app.route("/challenge/<string:challenge_uuid>", methods=["GET", "POST"])
def challenge(challenge_uuid):
    if request.method == "GET":
        if collection_exists(challenge_uuid, db_challenges):
            challenge_content = get_challenge_content(challenge_uuid, db_challenges)
            extend_deletion_date(db_sfxchallenge, challenge_uuid)
            return render_template("challenge.html", json_obj=challenge_content)
        else:
            return render_template("challenge_non_existent.html")
    if request.method == "POST":
        sfx_id = str(request.form.get("sfx_id"))
        guess = str(request.form.get("guess"))
        return compare_answer_to_game_name_by_id(challenge_uuid, db_challenges, sfx_id, guess)


@app.route("/challenge/<string:challenge_uuid>/result", methods=["POST"])
def challenge_results(challenge_uuid):
    if request.method == "POST":
        challenge_results_content = get_challenge_results_content(challenge_uuid, db_challenges)
        return jsonify(challenge_results_content)


@app.route("/audio/<string:audio_file_name>")
def return_audio_file(audio_file_name):
    base_path = Path(__file__).parent
    audio_file_path = os.path.join(base_path, "audio", audio_file_name + ".mp3")
    return send_file(
        audio_file_path,
        mimetype="audio/mp3",
        as_attachment=False,)


@app.route("/deletion/<string:deletion_uuid>", methods=["DELETE"])
def delete_challenges(deletion_uuid):
    if deletion_uuid == os.getenv("DELETION_KEY"):
        return delete_outdated_challenges(db_challenges, db_sfxchallenge)
    else:
        return '', 204


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def page_not_found(e):
    print(f"Error handler: {e}")  # todo Remove this line before deploying
    print(f"{request.script_root}/{request.path}")  # todo Remove this line before deploying
    return redirect(url_for("create_new_modern_challenge"), code=302)


##############################
# todo Add virtual fingerprint
##############################
# todo Add multiplayer option by utilizing websockets
##############################
# todo Redo the front page
##############################
# todo Start populating the database


if __name__ == '__main__':
    app.run(debug=True)

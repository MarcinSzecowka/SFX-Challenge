from flask import Flask, request, url_for, redirect, jsonify, render_template, send_file, send_from_directory
from database import connect_to_mongodb, get_collection
from utils import create_new_challenge, compare_answer_to_game_name_by_id, get_challenge_content, \
    get_challenge_results_content, collection_exists, add_deletion_date, delete_outdated_challenges, \
    extend_deletion_date, CreateChallengeForm, get_audio_file_path
from sounds import populate_sounds_collection
from error_messages import challenge_does_not_exist
from pathlib import Path
import os
import logging
import datetime

# Databases
db_sfxchallenge = connect_to_mongodb("SFXChallenge")
db_challenges = connect_to_mongodb("Challenges")

sounds_collection = get_collection(db_sfxchallenge, "Sounds")
sounds_collection.drop()
sounds_collection = get_collection(db_sfxchallenge, "Sounds")
populate_sounds_collection(sounds_collection)

# Logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                    datefmt="%m-%d %H:%M",
                    filename=os.path.join(os.path.abspath(os.curdir), f"logs\Debug{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log"),
                    filemode="w")
console = logging.StreamHandler()

# App
app = Flask(__name__)


@app.route("/")
def return_homepage():
    return redirect(url_for("create_new_modern_challenge"), code=302)


@app.route("/create/modern", methods=["GET", "POST"])
def create_new_modern_challenge(error_message=None):
    form = CreateChallengeForm(request.form)
    if request.method == "GET":
        if not error_message:
            return render_template("create_new_challenge.html", form=form, error_message=error_message)
        return render_template("create_new_challenge.html", form=form)
    if request.method == "POST" and form.validate():
        amount = form.question_amount.data
        min_year = form.minimum_year.data
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
            return render_template("create_new_challenge.html", error_message=challenge_does_not_exist)
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
    audio_file_path = get_audio_file_path(audio_file_name, db_sfxchallenge)
    audio_file_path = os.path.join(base_path, "audio", audio_file_path + ".mp3")
    return send_file(
        audio_file_path,
        mimetype="audio/mp3",
        as_attachment=False,)


@app.route("/deletion/<string:deletion_uuid>", methods=["DELETE"])
def delete_challenges(deletion_uuid):
    if deletion_uuid == os.getenv("DELETION_KEY"):
        return delete_outdated_challenges(db_challenges, db_sfxchallenge)
    else:
        return '', 401


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("create_new_modern_challenge"), code=302)


if __name__ == '__main__':
    app.run()

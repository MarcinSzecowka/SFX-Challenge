from uuid import uuid4
from database import connect_to_mongodb, create_challenge_collection


def select_random_sounds(amount, min_year):
    # todo dict below should be generated randomly from a previous collection containing every sfx
    sounds_dict = {
        "sound1": {
            "sound1_id": "example_sound1_id",
            "sound1_game_name": "example_game_name",
            "sound1_associated_file": "example_associated_file"
        },
        "sound2": {
            "sound1_id": "example_sound1_id",
            "sound1_game_name": "example_game_name",
            "sound1_associated_file": "example_associated_file"
        }
    }
    # todo select <amount> questions where year > <min_year> and add them to local dict
    return sounds_dict


def create_new_challenge(amount, min_year):
    challenge_uuid = str(uuid4())
    sounds = select_random_sounds(amount, min_year)
    db_challenges = connect_to_mongodb("Challenges")
    create_challenge_collection(challenge_uuid, db_challenges, sounds)
    return challenge_uuid

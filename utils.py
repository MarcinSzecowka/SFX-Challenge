def select_random_sounds(amount, min_year):
    sounds_dict = {}
    # todo select <amount> questions where year > <min_year> and add them to local dict
    return sounds_dict


def create_new_challenge(amount, min_year):
    challenge_uuid = "example_uuid_here"  # todo generate new uuid
    sounds = select_random_sounds(amount, min_year)
    # todo add new collection to database - col name should be the uuid, with <sounds> as its content
    return challenge_uuid

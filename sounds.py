def populate_sounds_collection(collection):
    # in "status" a 0 is the default value and it means the user has not yet tried to guess the game name
    # 1 means the user has correctly guessed the game name
    # 2 means the user tried to guess the name but was unsuccessful
    sounds_list = [
        {
            "_id": "f9e62f49-85af-4e1a-9259-505a185626e3",
            "game_name": "example_game_name1",
            "game_year": 2020,
            "associated_file": "example_associated_file1",
            "status": 0
        },
        {
            "_id": "1def231e-6a3d-43c1-9d25-c18cc306dda4",
            "game_name": "example_game_name2",
            "game_year": 2019,
            "associated_file": "example_associated_file2",
            "status": 0
        },
        {
            "_id": "bd3dc90a-dbdf-43a4-ae99-cfef7cfded73",
            "game_name": "example_game_name3",
            "game_year": 2018,
            "associated_file": "example_associated_file3",
            "status": 0
        },
        {
            "_id": "0771f838-08f8-4ade-844e-8d33b48277da",
            "game_name": "example_game_name4",
            "game_year": 2021,
            "associated_file": "example_associated_file4",
            "status": 0
        }
    ]
    results = collection.insert_many(sounds_list)

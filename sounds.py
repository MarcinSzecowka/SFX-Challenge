def populate_sounds_collection(collection):
    sounds_list = [
        {
            "_id": "81560d3e-7a22-4785-8782-2ba3eb2768fb",
            "game_name": "Battlefield 3",
            "game_year": 2011,
            "associated_file": "4769fb85-6aac-4606-a149-cceb8dc9c4f4",
            "status": "no_guess",
            "description": "Battlefield 3 fighter jet sound"
        },
        {
            "_id": "1def231e-6a3d-43c1-9d25-c18cc306dda4",
            "game_name": "Battlefield 3",
            "game_year": 2011,
            "associated_file": "3f7d811b-e510-4750-be45-eabe2e2462be",
            "status": "no_guess",
            "description": "Battlefield 3 fighter jet startup sound"
        },
        {
            "_id": "bd3dc90a-dbdf-43a4-ae99-cfef7cfded73",
            "game_name": "Call of Duty Warzone",
            "game_year": 2020,
            "associated_file": "1e03856d-3f22-4d95-a725-e91794cdc465",
            "status": "no_guess",
            "description": "CoD Warzone HS sound"
        },
        {
            "_id": "74461e20-52b5-4f5a-8dcc-49b396b3b60d",
            "game_name": "Crisis",
            "game_year": 2007,
            "associated_file": "ba0dbd11-2e47-4fed-b899-facdd1364b7d",
            "status": "",
            "description": "Crisis cloak engaged"
        },
        {
            "_id": "a88263ba-4b1b-41c8-b33f-10ab3b09ae33",
            "game_name": "Crisis",
            "game_year": 2007,
            "associated_file": "dbb77349-b8dc-49f0-9ef4-833df290ce88",
            "status": "",
            "description": "Crisis Maximum armour"
        },
        {
            "_id": "c9afa28b-3abf-4548-ae7c-7ab99b2bb14e",
            "game_name": "Crisis",
            "game_year": 2007,
            "associated_file": "53a7ba07-f283-44fe-81cd-08737558182c",
            "status": "",
            "description": "Crisis Maximum speed"
        },
        {
            "_id": "374cd12f-d4f6-4253-bb89-72289133a4d7",
            "game_name": "Crisis",
            "game_year": 2007,
            "associated_file": "23a47b79-f628-47ce-8966-ce17b3c3692c",
            "status": "",
            "description": "Crisis Maximum strength"
        },
        {
            "_id": "b21230d6-1da9-48d0-9224-83e1c09a146b",
            "game_name": "Counter strike Global offensive",
            "game_year": 2012,
            "associated_file": "8fddc276-7772-4ece-864e-06a07d81fb45",
            "status": "",
            "description": "CSGO Bomb detonation"
        },
        {
            "_id": "de7b29e4-5cc9-4c04-ac41-595ceb2a4a61",
            "game_name": "Counter strike Global offensive",
            "game_year": 2012,
            "associated_file": "d6b25d5c-e3f9-4248-a53a-9f5a99f6748a",
            "status": "",
            "description": "CSGO HS"
        },
        {
            "_id": "17e63b76-a58c-4b5a-876e-d70646ad6c8d",
            "game_name": "Diablo 2",
            "game_year": 2000,
            "associated_file": "93c46e7b-540f-4061-9fbc-408f908b86cf",
            "status": "",
            "description": "Diablo 2 level up sound"
        },
        {
            "_id": "026edb26-89bc-4cd3-b642-0d07d457e813",
            "game_name": "Diablo 2",
            "game_year": 2000,
            "associated_file": "ef6dbd9d-06c4-4fa4-9199-bd00bf094ea5",
            "status": "",
            "description": "Diablo 2 Gold drop sound"
        },
        {
            "_id": "ecd68a8e-674e-4b03-93bc-ceaca6f1387a",
            "game_name": "Diablo 3",
            "game_year": 2012,
            "associated_file": "ad4b6483-818e-4655-97d1-17178d05cdfb",
            "status": "",
            "description": "Diablo 3 legendary drop"
        },
        {
            "_id": "50615ec7-a7a9-4340-9c8e-02a5ecc1ba60",
            "game_name": "Dishonored",
            "game_year": 2012,
            "associated_file": "7d8d315d-24e3-43ff-8fff-7f23cafac69e",
            "status": "",
            "description": "Dishonored blink"
        },
        {
            "_id": "caac4db1-da21-4a62-a9f5-d4300fd75e99",
            "game_name": "Dota 2",
            "game_year": 2013,
            "associated_file": "25ab8fa3-1890-4132-8cf4-1cb4c6e08a33",
            "status": "",
            "description": "Dota 2 Queue pop"
        },
        {
            "_id": "28498965-d019-4ba8-9e31-2ad9ca93f1b2",
            "game_name": "Escape from Tarkov",
            "game_year": 2017,
            "associated_file": "16f31b91-5b43-416f-bba2-a1ea15bf6d09",
            "status": "",
            "description": "EFT container search"
        },
        {
            "_id": "408e32ed-f29d-4368-a336-140c1fc9f5df",
            "game_name": "Grand Theft Auto 4",
            "game_year": 2008,
            "associated_file": "115db6a9-d762-4abf-9536-a1b4b3a9687e",
            "status": "",
            "description": "GTA 4 menu sounds"
        },
        {
            "_id": "7303a597-0108-4a3a-b4de-1a11b54d2cc8",
            "game_name": "Left 4 Dead 2",
            "game_year": 2009,
            "associated_file": "848f1a67-e86b-42f1-8c14-3e42f8448919",
            "status": "",
            "description": "L4D2 Jockey"
        },
        {
            "_id": "a63794cc-a0c8-43ae-9570-1d3713817ecf",
            "game_name": "Left 4 Dead 2",
            "game_year": 2009,
            "associated_file": "da0ad8e1-e660-43f2-95bb-5b508eb9f07b",
            "status": "",
            "description": "L4D2 Witch"
        },
        {
            "_id": "c6b27bb6-4f61-488c-95a8-02d1a4f3dfea",
            "game_name": "League of Legends",
            "game_year": 2009,
            "associated_file": "7f1c339e-fadd-49f0-aa28-abbd3e4e2aae",
            "status": "",
            "description": "LOL arcane comet"
        },
        {
            "_id": "66f98ee2-9800-4134-ae6a-027350eb09bb",
            "game_name": "League of Legends",
            "game_year": 2009,
            "associated_file": "ef80c767-c173-4647-a79c-55b59bbc2300",
            "status": "",
            "description": "LOL electrocute"
        },
        {
            "_id": "fc51f9ef-7b0d-477c-9125-ad0080dd7d26",
            "game_name": "League of Legends",
            "game_year": 2009,
            "associated_file": "90161ae3-3719-4f81-bc3a-eb8e952b46fe",
            "status": "",
            "description": "LOL nexus explode"
        },
        {
            "_id": "5fbfafa1-7675-4798-bcc1-de5e2a603c22",
            "game_name": "League of Legends",
            "game_year": 2009,
            "associated_file": "295473b7-4242-4f22-9972-e1da670e2c57",
            "status": "",
            "description": "LOL queue pop"
        },
        {
            "_id": "4c897053-04ed-443c-9306-68c74f328871",
            "game_name": "Minecraft",
            "game_year": 2011,
            "associated_file": "9a3d360e-ee5f-40de-a998-8a0d8e2324a0",
            "status": "",
            "description": "Minecraft Gravel"
        },
        {
            "_id": "864672eb-e21e-4f13-bab3-185b65af3da4",
            "game_name": "Minecraft",
            "game_year": 2011,
            "associated_file": "c22db91a-4226-47d9-9774-5af0acb1acc2",
            "status": "",
            "description": "Minecraft Level up"
        },
        {
            "_id": "f5f670d3-8049-46ec-9455-f17e16267ccd",
            "game_name": "Minecraft",
            "game_year": 2011,
            "associated_file": "abd8f390-66d3-467b-93d8-95ca360f4473",
            "status": "",
            "description": "Minecraft stone"
        },
        {
            "_id": "ec097b61-d745-49d2-bc3b-0663ee595313",
            "game_name": "Minecraft",
            "game_year": 2011,
            "associated_file": "63221224-6f8c-4499-a1e1-8fdb33184da8",
            "status": "",
            "description": "Minecraft wood"
        },
        {
            "_id": "9457793e-63ee-4ab5-a48e-3b43e646b846",
            "game_name": "MU Online",
            "game_year": 2001,
            "associated_file": "12afbd7b-c36c-4819-b8e7-ec6c6acd68f2",
            "status": "",
            "description": "Mu devias worm growl"
        },
        {
            "_id": "6edfb690-46a7-4f7f-9379-2271da39aa93",
            "game_name": "Path of Exile",
            "game_year": 2013,
            "associated_file": "14463c57-cc5a-4c5b-8aff-85763424005a",
            "status": "",
            "description": "PoE chaos drop sound"
        },
        {
            "_id": "4d7ba312-fc65-4a6c-b87f-caf3eb100c7c",
            "game_name": "Path of Exile",
            "game_year": 2013,
            "associated_file": "cc08f111-601c-4d43-86bd-f133b168024a",
            "status": "",
            "description": "PoE ex drop sound"
        },
        {
            "_id": "9e2d3034-7eb6-42e0-88d9-091d6c2f5cde",
            "game_name": "Portal",
            "game_year": 2007,
            "associated_file": "e5451b85-43ec-4155-96bb-1ba10236bf5c",
            "status": "",
            "description": "Portal blue portal"
        },
        {
            "_id": "39a234ee-52d7-4b68-b822-4106fe832a79",
            "game_name": "Portal",
            "game_year": 2007,
            "associated_file": "d3a17694-c105-48b9-a933-868abca7d1b6",
            "status": "",
            "description": "Portal orange portal"
        },
        {
            "_id": "ceb892fc-7b32-4543-829f-9b7aea1d314f",
            "game_name": "PUBG",
            "game_year": 2017,
            "associated_file": "d6101307-db51-4746-8520-44cf8f1ca8c2",
            "status": "",
            "description": "PUBG airplane sound"
        },
        {
            "_id": "fd813bd2-beea-4704-87e2-8eb397a580b9",
            "game_name": "Old school RuneScape",
            "game_year": 2007,
            "associated_file": "befffe96-e80d-41cb-9797-96f3b94624d6",
            "status": "",
            "description": "OSRS casting spells"
        },
        {
            "_id": "d672d1cc-5b4c-4bd2-bfa9-a37987da3915",
            "game_name": "Old school RuneScape",
            "game_year": 2007,
            "associated_file": "77c7a015-095f-4150-bc7e-72aaec560453",
            "status": "",
            "description": "OSRS getting hit"
        },
        {
            "_id": "d6fb7322-ef4e-4a95-9ee1-b8078d2299c1",
            "game_name": "Rust",
            "game_year": 2013,
            "associated_file": "183f681b-f1b3-4312-8e2e-f3a0f143f0a0",
            "status": "",
            "description": "Rust breaking rock"
        },
        {
            "_id": "51ad510b-c1ae-4d1c-89e7-ca1bd9ed9aac",
            "game_name": "Rust",
            "game_year": 2013,
            "associated_file": "f9a1eae8-c9b2-4388-9351-9ed2f547f7a5",
            "status": "",
            "description": "Rust hitting tree"
        },
        {
            "_id": "793fd78d-6c8e-4c95-bb7a-413ec91c4e84",
            "game_name": "The Elder Scrolls V: Skyrim",
            "game_year": 2011,
            "associated_file": "31b459c8-d930-4c80-a451-e3dc5b09da80",
            "status": "",
            "description": "Skyrim level up"
        },
        {
            "_id": "d0634c9e-e425-4e14-90bf-742ba0f9fb9f",
            "game_name": "The Elder Scrolls V: Skyrim",
            "game_year": 2011,
            "associated_file": "d3ff395e-df32-4d34-8766-445c028d9c14",
            "status": "",
            "description": "Skyrim quest complete"
        },
        {
            "_id": "eb78441d-3e30-4832-8f4b-0671167dd28b",
            "game_name": "The Elder Scrolls V: Skyrim",
            "game_year": 2011,
            "associated_file": "cc5ab06c-cfe5-4633-9af9-90184a2084db",
            "status": "",
            "description": "Skyrim soul absorb"
        },
        {
            "_id": "95e00b8c-1659-499c-aa20-f61764ddf767",
            "game_name": "Sniper Elite v2",
            "game_year": 2012,
            "associated_file": "86811beb-5d3e-4418-b9eb-dbdc948fdd93",
            "status": "",
            "description": "Sniper elite v2 Breath holding sound"
        },
        {
            "_id": "e14c9196-11d0-4eee-ad2e-e26de3cfa295",
            "game_name": "Sniper Elite v2",
            "game_year": 2012,
            "associated_file": "a0934ff4-0271-4588-8955-92c12863c9e3",
            "status": "",
            "description": "Sniper elite v2 skull crush"
        },
        {
            "_id": "c671873a-9763-4dfc-96b6-7c2c71947889",
            "game_name": "Starcraft",
            "game_year": 1998,
            "associated_file": "65f48b1e-1423-4811-ae44-577e269d390e",
            "status": "",
            "description": "Starcraft protoss building"
        },
        {
            "_id": "499d84da-d3e6-4564-9e1a-68ad63f94aa5",
            "game_name": "Terraria",
            "game_year": 2011,
            "associated_file": "50f2cf60-a235-4be3-8594-341db6c572af",
            "status": "",
            "description": "Terraria boss summon"
        },
        {
            "_id": "12611ec2-33a9-41b6-a3b9-8cb7dd8773d6",
            "game_name": "Terraria",
            "game_year": 2011,
            "associated_file": "4615df93-9764-40a1-ba8e-f7b2d3a85a0a",
            "status": "",
            "description": "Terraria getting hurt"
        },
        {
            "_id": "672f0bf9-b5b1-4085-8d42-dfd98ea1af48",
            "game_name": "Terraria",
            "game_year": 2011,
            "associated_file": "24ca5ae6-9e23-46cb-8b25-e33b5d79b2f9",
            "status": "",
            "description": "Terraria shooting a bow"
        },
        {
            "_id": "8210fd0e-54e1-4ace-a7b0-d892eb3c1c32",
            "game_name": "Terraria",
            "game_year": 2011,
            "associated_file": "3e3d688f-0068-4b41-aa72-8fbbb02e2569",
            "status": "",
            "description": "Terraria sword swing"
        },
        {
            "_id": "ccd6016b-b2ad-4ed4-8325-e100c727a0f7",
            "game_name": "World of Tanks",
            "game_year": 2010,
            "associated_file": "f26a2779-f888-4bbb-a13b-fb18a27a9f2c",
            "status": "",
            "description": "WoT getting hit"
        },
        {
            "_id": "8371d8e8-4cc8-41a6-ae51-d21af67544a0",
            "game_name": "World of Tanks",
            "game_year": 2010,
            "associated_file": "04044b37-57a4-4668-94f4-842dc88404fd",
            "status": "",
            "description": "WoT tank shots"
        },
        {
            "_id": "838cf048-f4fe-49ed-8cd4-df73a2e67bc5",
            "game_name": "World of Warcraft",
            "game_year": 2004,
            "associated_file": "98622a5d-289a-4255-aeb3-e454d5c59e0a",
            "status": "",
            "description": "WoW lust"
        },
        {
            "_id": "5d4afafe-7ad2-44dc-b94a-8eb8aca9c676",
            "game_name": "World of Warcraft",
            "game_year": 2004,
            "associated_file": "91fa5f31-39dc-4a8c-bb8d-f10228618861",
            "status": "",
            "description": "WoW level up"
        },
        {
            "_id": "0ad45bcc-5647-46f1-b4d1-c7a8b3cb4b85",
            "game_name": "World of Warcraft",
            "game_year": 2004,
            "associated_file": "234ef9e9-0415-4614-9d4d-6f57e4ce3052",
            "status": "",
            "description": "WoW Quest complete"
        },
        {
            "_id": "aa62c2cb-0315-4b77-a047-795d273f4f7e",
            "game_name": "World of Warcraft",
            "game_year": 2004,
            "associated_file": "a2dc7acf-ce24-47a8-bc38-dee8f2791e12",
            "status": "",
            "description": "WoW stealth"
        },
    ]
    # noinspection PyUnusedLocal
    insertion_id = collection.insert_many(sounds_list)


# {
#             "_id": "",
#             "game_name": "",
#             "game_year": 0,
#             "associated_file": "",
#             "status": "",
#             "description": "CoD Warzone HS sound"
#         },

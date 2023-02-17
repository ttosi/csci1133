locations = {
    "room1": {
        "text": "You are in room one.\nThe room is dark and cold with no windows.\nYou have no memory of how you got here.",
        "is_end": False,
        "options": {
            "a": {"text": "go to room 2", "goes_to": "room2"},
            "c": {"text": "go to room 3", "goes_to": "room3"},
        },
    },
    "room2": {
        "text": "You are in room two.",
        "is_end": False,
        "options": {
            "a": {"text": "go to room 5", "goes_to": "room5"},
            "b": {"text": "go to room 6", "goes_to": "room6"},
            "c": {"text": "go to room 4", "goes_to": "room4"},
        },
    },
    "room3": {
        "text": "You are in room three.",
        "is_end": False,
        "options": {
            "a": {"text": "go to room 2", "goes_to": "room2"},
            "b": {"text": "go to room 4", "goes_to": "room4"},
            "c": {"text": "go to room 3", "goes_to": "room3"},
            "d": {"text": "go to room 5", "goes_to": "room5"},
            "e": {"text": "go to room 1", "goes_to": "room1"},
        },
    },
    "room4": {
        "text": "You are in room four.",
        "is_end": False,
        "options": {
            "a": {"text": "go to room 1", "goes_to": "room1"},
            "b": {"text": "go to room 5", "goes_to": "room5"},
            "c": {"text": "go to room 8", "goes_to": "room8"},
        },
    },
    "room5": {
        "text": "You are in room five.",
        "is_end": False,
        "options": {
            "a": {"text": "go to room 1", "goes_to": "room1"},
            "b": {"text": "go to room 7", "goes_to": "room7"},
            "c": {"text": "go to room 6", "goes_to": "room6"},
        },
    },
    "room6": {
        "text": "You are in room six.",
        "is_end": False,
        "options": {
            "a": {"text": "go to room 1", "goes_to": "room1"},
            "b": {"text": "go to room 5", "goes_to": "room5"},
            "c": {"text": "go to room 3", "goes_to": "room3"},
        },
    },
    "room7": {"text": "The game is now over, you win!", "is_end": True},
    "room8": {"text": "The game is now over, you lose.", "is_end": True},
}

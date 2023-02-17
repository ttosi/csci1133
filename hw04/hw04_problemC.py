# this variable (it's just one big variable, a dictionary) defines
# the choices a player can make. i used rooms instead of a storyline because
# it was easier for me to visualize. each "room" in my case just represensts
# the state of where the user is at in the flowchart. it looks crazy, i know.
# but, check it out. if i wanted to know about 'room2', i could say print(choices["room2"]) and I
# would get all of the data only under room2. if I wanted to know where a user would go if
# they chose option 'c' while they were in 'room2' i could print(choices["room2"]["options"]["c"]["goes_to"])
# which would output "room4". see how the text in the brackets just maps it to what i want to retrieve?
# the cool part is i don't have to use the "hard coded" names, I can use another variable
# so if a user selects option 'a' while in room1, eg, user_choice = input("make a selecttion: ") and they enter 'a'
# i can do print(choices["room1"]["options"][user_choice]) and bam, now I know what the next
# room they chose to go to is! if you look at the flow chart in the assignment you can notice
# how this is just a representation of it (i did room1 on the top decision, room2 on the left, room3 on the right
# and room4 on the bottom decision).
choices = {
    "room1": {
        "text": "You are in room one.",
        "options": {
            "a": {"text": "go to room 2", "goes_to": "room2"},
            "b": {"text": "go to room 5", "goes_to": "room5"},
            "c": {"text": "go to room 3", "goes_to": "room3"},
        },
    },
    "room2": {
        "text": "You are in room two.",
        "options": {
            "a": {"text": "go to room 5", "goes_to": "room5"},
            "b": {"text": "go to room 6", "goes_to": "room6"},
            "c": {"text": "go to room 4", "goes_to": "room4"},
        },
    },
    "room3": {
        "text": "You are in room three.",
        "options": {
            "a": {"text": "go to room 2", "goes_to": "room2"},
            "b": {"text": "go to room 4", "goes_to": "room4"},
            "c": {"text": "go to room 3", "goes_to": "room3"},
            "c": {"text": "go to room 5", "goes_to": "room5"},
            "c": {"text": "go to room 1", "goes_to": "room1"},
        },
    },
    "room4": {
        "text": "You are in room four.",
        "options": {
            "a": {"text": "go to room 1", "goes_to": "room1"},
            "b": {"text": "go to room 5", "goes_to": "room5"},
            "c": {"text": "go to room 6", "goes_to": "room6"},
        },
    },
    "room5": {
        "text": "You are in room five.",
        "options": {
            "a": {"text": "go to room 1", "goes_to": "room1"},
            "b": {"text": "go to room 2", "goes_to": "room2"},
            "c": {"text": "go to room 6", "goes_to": "room6"},
        },
    },
    "room6": {
        "text": "You are in room six.",
        "options": {
            "a": {"text": "go to room 1", "goes_to": "room1"},
            "b": {"text": "go to room 5", "goes_to": "room5"},
            "c": {"text": "go to room 3", "goes_to": "room3"},
        },
    },
}


def adventure(room_name):
    """
    Returns:
      The name of the next room (string) or a bool representing a good or bad ending
    """
    if room_name == True or room_name == False:
        return room_name

    # so now that i know the room name, i can get all the info I need to call choose_three()
    text = choices[room_name]["text"]
    optionA = choices[room_name]["options"]["a"]["text"]
    optionB = choices[room_name]["options"]["b"]["text"]
    optionC = choices[room_name]["options"]["c"]["text"]

    choice = choose_three(text, optionA, optionB, optionC)

    return choices[room_name]["options"][choice]["goes_to"]


def choose_three(text, optionA, optionB, optionC):
    print("".rjust(len(text) + 4, "-"))
    print("| " + text + " |")
    print("".rjust(len(text) + 4, "-"))
    print("(a) " + optionA)
    print("(b) " + optionB)
    print("(c) " + optionC)

    valid_value = False
    while not valid_value:
        val = input("What is your choice (a, b, or c)? ")
        if val == "a" or val == "b" or val == "c":
            valid_value = True
        else:
            print("Invalid option, try again")

    return val


if __name__ == "__main__":
    choice = adventure("room1")  # start it off at the first room

    # keep going until make_choice() isn't true or false (otherwise,
    # make_choice will return the name of the next room the player selected)
    while choice != True and choice != False:
        choice = adventure(choice)

    # made it here because make_choice() returned a bool
    if choice:
        print("Good, you made it!")
    else:
        print("Bad, I'm sorry :(")

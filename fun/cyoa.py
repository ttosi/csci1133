from cyoa_data import locations


def print_boxed(text):
    lines = text.split("\n")
    longest_line = max(lines, key=len)

    print("-" * (len(longest_line) + 4))
    for line in lines:
        print("| " + line + " " * (len(longest_line) - len(line)) + " |")
    print("-" * (len(longest_line) + 4))


def choose_one(location):
    for option in location["options"]:
        print(f"({option}) {location['options'][option]['text']}")

    print("")
    while True:
        choice = input("What is your choice (q to quit)? ")
        if choice == "q":
            exit()
        for option in location["options"]:
            if option == choice:
                return location["options"][choice]["goes_to"]

        print("Invalid option, please try again")


def next_location(room_name):
    return choose_one(locations[room_name])


print_boxed(locations["room1"]["text"])
location = next_location("room1")

while not locations[location]["is_end"]:
    print_boxed(locations[location]["text"])
    location = next_location(location)

print_boxed(locations[location]["text"])

from problemA import durdle_match

invalid_chars = "1234567890`~!@#$%^&*()_-=+[]{}|\;':<>,./? ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def check_valid_chars(target):
    is_valid = True
    for target_char in target:
        for invalid_char in invalid_chars:
            if target_char == invalid_char:
                is_valid = False
    return is_valid

def durdle_game(target):
    game_over = False
    num_guesses = 0
    target_len = len(target)

    print("Welcome to Durdle! The target word has " + str(target_len) + " letters.")

    while not game_over:
        valid_input = False
        while not valid_input:
            guess = input("Enter a guess: ")
            if len(guess) == target_len and check_valid_chars(guess):
                valid_input = True
            else:
                print("Invalid guess.")

        guess_string = durdle_match(guess, target)
        num_guesses += 1

        guessed = True
        for char in guess_string:
            if char != "G":
                guessed = False
        # OR this way, does same thing as above just in one line
        # guessed = guess_string == "G" * target_len

        if guessed == True:
            game_over = True
            print("Congratulations, you got it in " + str(num_guesses) + " guesses!")
        else:
          print("               " + guess_string)

if __name__ == "__main__":
    durdle_game("parameter")

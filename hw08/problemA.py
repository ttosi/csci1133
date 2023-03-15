def durdle_match(guess, target):
    result = ""
    for guess_pos in range(len(guess)):
        if guess[guess_pos] == target[guess_pos]:
            result += "G"
        elif guess[guess_pos] != target[guess_pos]:
            has_char = False
            for target_char in target:
                if guess[guess_pos] == target_char:
                    has_char = True
            if has_char == True:
                result += "Y"
            else:
                result += "B"

    return result


if __name__ == "__main__":
    print(durdle_match("quick", "perky"), "\t", durdle_match("quick","perky") == "BBBBY")  # 'BBBBY'
    print(durdle_match("test", "deft"), "\t", durdle_match("test", "deft") == "YGBG")  # 'YGBG'
    print(durdle_match("wizard", "zicron"), "\t", durdle_match("wizard", "zicron") == "BGYBYB")  # 'BGYBYB'
    print(durdle_match("parry", "perky"), "\t", durdle_match("parry", "perky") == "GBGYG")  # 'GBGYG'
    print(durdle_match("guessing", "guessing"), durdle_match("guessing", "guessing") == "GGGGGGGG")  # 'GGGGGGGG'

def durdle_match(guess, target):
    result = ""
    pos = 0
    for guess_char in guess:
        if target.find(guess_char, pos) == pos:
            result += "G"
        elif target.find(guess_char) > -1:
            result += "Y"
        else:
            result += "B"
        pos += 1

    return result


if __name__ == "__main__":
    print(durdle_match("quick", "perky"))  # 'BBBBY'
    print(durdle_match("test", "deft"))  # 'YGBG'
    print(durdle_match("wizard", "zicron"))  # 'BGYBYB'
    print(durdle_match("parry", "perky"))  # 'GBGYG'
    print(durdle_match("guessing", "guessing"))  # 'GGGGGGGG'

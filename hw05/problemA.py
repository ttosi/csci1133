def greater_by_one_for(a_string):
    result = ""
    for char in a_string:
        val = int(char)

        if val == 9:
            val = 0
        else:
            val += 1

        result += str(val)

    return result


def greater_by_one_while(a_string):
    result = ""
    index = 0
    while index < len(a_string):
        val = int(a_string[index])

        if val == 9:
            val = 0
        else:
            val += 1

        result += str(val)
        index += 1

    return result


if __name__ == "__main__":
    print(greater_by_one_for(""))  # ""
    print(greater_by_one_while(""))  # ""
    print(greater_by_one_for("123"))  # "234"
    print(greater_by_one_for("234"))  # '345'
    print(greater_by_one_while("234"))  # '345'
    print(greater_by_one_for("93023"))  # '04134'
    print(greater_by_one_while("93023"))  # '04134'

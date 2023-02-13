def choose_three(text, optionA, optionB, optionC):
    """
    Purpose:
      Given a prompt and three options, allow the user
      to choose one of the three options
    Parameter(s):
      text: prompt (string)
      optionA: the first option (string)
      optionB: the second option (string)
      optionC: the third option (string)
    Return Value:
      a valid user input of A or B or C (string)
    """
    print(text)
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
    print("You chose option " + choose_three("text", "a", "b", "c"))

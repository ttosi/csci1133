def choose_three(text, optionA, optionB, optionC):
    """
    Purpose:
      Given a prompt and three options, allow the user
      to choose one of the three options
    Paramater(s):
      text: prommpt (string)
      optionA: the first option (string)
      optionB: the second option (string)
      optionC: the third option (string)
    Return Value:
      a valid user input of A or B or C (string)
    """
    print(text)
    print("(A) " + optionA)
    print("(B) " + optionB)
    print("(C) " + optionC)

    while True:
        val = input("What is your choice (A, B, or C)? ")
        if val == "A" or val == "B" or val == "C":
            return val

        print("Invalid option, try again")


if __name__ == "__main__":
    print("You chose option " + choose_three("text", "a", "b", "c"))

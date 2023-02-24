def word_mix(wordList1, wordList2):
    result = ""

    if len(wordList1) >= len(wordList2):
        for i in range(len(wordList1)):
            if i < len(wordList2):
                result += wordList1[i] + " " + wordList2[i] + " "
            else:
                result += wordList1[i] + " "
    else:
        for i in range(len(wordList2)):
            if i < len(wordList1):
                result += wordList1[i] + " " + wordList2[i] + " "
            else:
                result += wordList2[i] + " "

    return result[: len(result) - 1]


if __name__ == "__main__":
    print(word_mix(["the", "brown"], ["quick", "fox"]))
    print(word_mix(["the", "brown", "jumped", "over"], ["quick", "fox"]))
    print(
        word_mix(
            ["the", "brown"], ["quick", "fox", "jumped", "over", "the", "lazy", "dogs"]
        )
    )

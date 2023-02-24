def larger_decrement(numList, n):
    found_index = 0
    tempNum = 0
    for i in range(len(numList)):
        if numList[i] > n and numList[i] > tempNum:
            tempNum = numList[i]
            found_index = i

    if found_index == 0:
        return False
    else:
        numList[found_index] = numList[found_index] - 1
        return True


if __name__ == "__main__":
    aList = [5, 20, 74, 81, 0, 81, 3]
    print(larger_decrement(aList, 50))
    print(aList)
    bList = [1, 3, 5]
    print(larger_decrement(bList, 6))
    print(bList)

def list_difference(numList1, numList2):
    result = []
    for i in range(len(numList1)):
        result.append(numList1[i] - numList2[i])

    return result


if __name__ == "__main__":
    aList = [5, 6, 7]
    bList = [2, 2, 2]
    print(list_difference(aList, bList))
    print(aList)
    print(bList)
    print(list_difference([0, 1, 1, 2], [3, 5, 8, 13]))
    print(list_difference([], []))

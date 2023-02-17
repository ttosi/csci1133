def count_of_sums(lower, upper, sum_val):
    count = 0
    for i in range(lower, upper + 1):  # add 1 to upper to make it inclusive
        for j in range(lower, upper + 1):
            # print(i, "+", j, "=", i + j)
            if i + j == sum_val:
                count += 1

    return count


if __name__ == "__main__":
    print(count_of_sums(2, 10, 8))  # 5
    print(count_of_sums(0, 15, 15))  # 16
    print(count_of_sums(-4, 8, 6))  # 11
    print(count_of_sums(5, 8, 30))  # 0

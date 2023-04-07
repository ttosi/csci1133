def collatz(n, total):
    total = total + n
    value = 0

    if n % 2 == 0:  # is even
        value = int(n / 2)
    else:  # is odd
        value = n * 3 + 1

    print("value", value, total)
    if n != 1:
        return collatz(value, total)
    else:
        print("total =", total)
        return total


if __name__ == "__main__":
    print(collatz(5, 0))

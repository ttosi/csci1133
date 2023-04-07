def collatz(n):
    value = 0

    if n % 2 == 0:  # is even
        value = int(n / 2)
    else:  # is odd
        value = n * 3 + 1

    if n != 1:
        return n + collatz(value)
    else:
        return n


if __name__ == "__main__":
    print(collatz(5))
    print(collatz(1))
    print(collatz(123))

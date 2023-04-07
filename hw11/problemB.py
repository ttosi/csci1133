def two_es(lines):
    if len(lines) == 0:
        return False

    line = lines[len(lines) - 1]
    if line.count("e") == 2:
        return True
    elif len(lines) - 1 != 0:
        lines.remove(lines[len(lines) - 1])
        return two_es(lines)

    return False


if __name__ == "__main__":
    print(two_es(["One line\n", "Two lines\n", "Three lines\n"]))
    print(
        two_es(["here is a line\n", "Another linE, starting with A\n", "One MorE linE"])
    )
    print(two_es([]))
    print(
        two_es(
            [
                "More examples\n",
                "Here there are two lines that work\n",
                "This is one of them\n",
                "This is not\n",
                "Excellent",
            ]
        )
    )

def most_populous(year, region):
    cities = []
    file = open("cities.csv", "r")
    file.readline()

    for line in file:
        data = line.split(",")
        if data[0] == year and data[4].replace("\n", "") == region:
            cities.append(data[1])
    file.close()

    return cities


if __name__ == "__main__":
    print(most_populous("1500", "East Asia"))
    print(most_populous("1673", "Europe"))
    print(most_populous("1499", "South Asia"))
    print(most_populous("1500", "USA"))

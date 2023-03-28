def stasis(jump_year, jump_city):
    original_cities = open("cities.csv", "r")
    fixed_cities = open("fixed_cities.csv", "w")
    original_cities.readline()

    city_count = 0
    for line in original_cities:
        data = line.split(",")
        if data[0] >= jump_year and data[1] == jump_city:
            data[3] = str(int(data[3]) + 3)
            city_count += 1
            fixed_cities.write(",".join(data))
        else:
            fixed_cities.write(",".join(data))

    original_cities.close()
    fixed_cities.close()

    return city_count


if __name__ == "__main__":
    print(stasis("1973", "London"))
    # print(stasis("1450", "Edirne"))
    # print(stasis("1798", "Suzhou"))

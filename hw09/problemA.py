def total_time(fname, employee):
    hours_worked = {}

    try:
        file = open(fname, "r")
    except FileNotFoundError:
        return -1.0

    for line in file:
        employee_time = line.split(" ")
        name = employee_time[0]
        hours = float(employee_time[1].replace("\n", ""))

        if name not in hours_worked.keys():
            hours_worked[name] = hours
        else:
            hours_worked[name] += hours
    file.close()

    if employee not in hours_worked.keys():
        return 0.0
    else:
        return hours_worked[employee]


if __name__ == "__main__":
    print(total_time("hours1.txt", "Leslie"))
    print(total_time("hours2.txt", "Jeff"))
    print(total_time("hours3.txt", "Tian"))
    print(total_time("fakefile.txt", "Nobody"))

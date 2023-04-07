import os


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


targets = []


def get_targets(path):
    for file in os.listdir(path):
        if os.path.isfile(path + "/" + file):
            if file.endswith(".txt"):
                # targets.append(path + "/" + file)
                target_path = path + "/" + file
                file = open(target_path, "r")
                lines = []
                for line in file:  # add all lines in file to list
                    lines.append(line)

                if two_es(lines) == True:
                    targets.append(target_path)
        else:
            get_targets(path + "/" + file)  # Go into a subdirectory

    return targets


if __name__ == "__main__":
    # print(get_targets("docs1"))
    # print(get_targets("docs2"))
    print(get_targets("docs3"))

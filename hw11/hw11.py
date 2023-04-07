import os

targets = []


def get_targets(path):
    for file in os.listdir(path):
        if os.path.isfile(path + "/" + file):
            if file.endswith(".txt"):
                targets.append(path + "/" + file)
        else:
            get_targets(path + "/" + file)  # Go into a subdirectory

    return targets

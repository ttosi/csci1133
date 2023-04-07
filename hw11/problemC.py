import os
from hw11 import get_targets
from problemB import two_es


targets = get_targets("docs2")
good_docs = []
for target in targets:
    file = open(target, "r")
    lines = []
    for line in file:  # add all lines in file to list
        lines.append(line)

    if two_es(lines) == True:
        good_docs.append(target)

print(good_docs)

if __name__ == "__main__":
    pass
    # print(get_targets("docs1"))

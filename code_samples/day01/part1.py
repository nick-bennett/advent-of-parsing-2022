def parse1(filename):
    with open(filename, "r") as fp:
        data = fp.read()

    all_calories = []
    for line in data.split("\n\n"):
        all_calories.append(line.splitlines())

    print(all_calories)


def parse2(filename):
    with open(filename, "r") as fp:
        data = fp.read().split("\n\n")

    all_calories = [line.splitlines() for line in data]
    print(all_calories)


def parse3(filename):
    with open(filename, "r") as fp:
        data = fp.read().split("\n\n")

    all_calories = []
    for line in data:
        all_calories.append([int(calorie) for calorie in line.splitlines()])

    print(all_calories)


if __name__ == "__main__":
    # parse1("./example.txt")
    # parse2("./example.txt")
    parse3("./example.txt")

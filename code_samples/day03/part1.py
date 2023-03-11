def parse1(filename):
    with open(filename, "r") as fp:
        rucksacks = fp.read()

    print(rucksacks.splitlines())


def parse2(filename):
    with open(filename, "r") as fp:
        rucksacks = fp.read().splitlines()

    print(rucksacks)


if __name__ == "__main__":
    parse1("./example.txt")
    parse2("./example.txt")

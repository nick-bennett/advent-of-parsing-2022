def parse1(filename):
    with open(filename, "r") as fp:
        data = fp.read()

    for round in data.splitlines():
        opponent_play, your_play = round.split()
        print(f"{opponent_play = }, {your_play =}")


def parse2(filename):
    with open(filename, "r") as fp:
        data = fp.read()

    rounds = [round.split() for round in data.splitlines()]
    print(rounds)


if __name__ == "__main__":
    parse1("./example.txt")
    parse2("./example.txt")

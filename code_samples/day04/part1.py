import re


def parse1(filename):
    with open(filename, "r") as fp:
        section_pairs = fp.read().splitlines()

    for pair in section_pairs:
        first_pair, second_pair = pair.split(",")
        first_init, first_end = first_pair.split("-")
        second_init, second_end = second_pair.split("-")

        print(
            f"first pair: {first_init}->{first_end}\tsecond pair: {second_init}->{second_end}"
        )


def parse2(filename):
    with open(filename, "r") as fp:
        section_pairs = fp.read().splitlines()

    ranges = []
    for pair in section_pairs:
        first_pair, second_pair = pair.split(",")
        ranges.append([first_pair.split("-"), second_pair.split("-")])

    print(ranges)


def parse3(filename):
    with open(filename, "r") as fp:
        section_pairs = fp.read().splitlines()

    ranges = []
    for pair in section_pairs:
        first_pair, second_pair = pair.split(",")
        first_init, first_end = first_pair.split("-")
        second_init, second_end = second_pair.split("-")

        ranges.append(
            [[int(first_init), int(first_end)], [int(second_init), int(second_end)]]
        )

    print(ranges)


def parse4(filename):
    with open(filename, "r") as fp:
        section_pairs = fp.read().splitlines()

    re_expr = r"(\d+)-(\d+),(\d+)-(\d+)"

    for line in section_pairs:
        expr_match = re.match(re_expr, line)
        first_init = expr_match.group(1)
        first_end = expr_match.group(2)
        second_init = expr_match.group(3)
        second_end = expr_match.group(4)

        print(
            f"first pair: {first_init}->{first_end}\tsecond pair: {second_init}->{second_end}"
        )


if __name__ == "__main__":
    parse1("./example.txt")
    parse2("./example.txt")
    parse3("./example.txt")
    parse4("./example.txt")

from math import prod

with open("day_03/input.txt") as f:
    entries = [line.strip() for line in f]


def part1(entries, right=3, down=1):
    return sum((1 for i, entry in enumerate(entries[::down]) if entry[i * right % len(entry)] == '#'))


def part2(entries, movements: (int, int)):
    return prod((part1(entries, movement[0], movement[1]) for movement in movements))


if __name__ == "__main__":
    print(part1(entries))
    print(part2(entries, {(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)}))

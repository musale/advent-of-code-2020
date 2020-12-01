from typing import Sequence


def part_one(arr: Sequence[int]) -> int:
    for n in arr:
        target = 2020 - n
        if target in nums:
            return n * target


if __name__ == "__main__":
    nums = [int(n) for n in open("day_01/input.txt").read().split("\n")]
    print(part_one(nums))

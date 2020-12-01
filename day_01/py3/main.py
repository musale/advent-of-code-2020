from typing import Sequence


def part_one(arr: Sequence[int]) -> int:
    for n in arr:
        target = 2020 - n
        if target in nums:
            return n * target


def part_two(arr: Sequence[int]) -> int:
    for i in arr:
        for j in arr[1:]:
            target = 2020 - i - j
            if target in arr[2:]:
                return i * j*target


if __name__ == "__main__":
    nums = [int(n) for n in open("day_01/input.txt").read().split("\n")]
    print(part_one(nums))
    print(part_two(nums))

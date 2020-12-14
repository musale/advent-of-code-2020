from typing import Tuple


def part_1(commands) -> Tuple[int, bool]:
    idx = 0
    command = commands[idx]
    visited = set()
    accumulator = 0
    has_loop = False
    while idx not in visited:
        visited.add(idx)
        instruction, op, value = command[:3], command[4:5], int(command[5:])
        if instruction == "nop":
            idx += 1
            command = commands[idx]
            continue
        if op == "-":
            value = value * -1
        if instruction == "acc":
            accumulator += value
            idx += 1
        elif instruction == "jmp":
            idx += value
        try:
            command = commands[idx]
            if idx in visited:
                has_loop = True
        except IndexError as err:
            break
    return accumulator, has_loop


def part_2(commands) -> int:
    accumulator = 0
    swapper = {"nop": "jmp", "jmp": "nop"}
    for idx, command in enumerate(commands):
        instruction = command[:3]
        if instruction in ["jmp", "nop"]:
            swapped = command.replace(instruction, swapper[instruction])
            accumulator, has_loop = part_1(
                commands[:idx]+[swapped]+commands[idx+1:])
            if not has_loop:
                return accumulator
    return accumulator


if __name__ == "__main__":
    with open("day_08/input.txt") as f:
        commands = [line.strip() for line in f.readlines()]
        print(f"Part 1: {part_1(commands)}")
        print(f"Part 2: {part_2(commands)}")

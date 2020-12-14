

class IntCode:
    def __init__(self):
        self.accumulator = 0
        self.visited = set()

    def jmp(self, command) -> int:
        operator, value = command[:1], int(command[1:])
        if ("jmp", command) in self.visited:
            print(f"Infinity loop detected at jmp {self.accumulator}")
            return self.accumulator
        if operator == "-":
            value = value * -1
        self.accumulator += value
        self.visited.add(("jmp", command))
        return self.accumulator

    def acc(self, command):
        operator, value = command[:1], int(command[1:])
        if ("acc", command) in self.visited:
            print(f"Infinity loop detected at acc {self.accumulator}")
            return self.accumulator
        if operator == "-":
            value = value * -1
        self.accumulator += value
        self.visited.add(("acc", command))
        return self.accumulator


if __name__ == "__main__":
    with open("day_08/input.txt") as f:
        commands = [line.strip() for line in f.readlines()]

    idx = 0
    command = commands[idx]
    visited = set()
    accumulator = 0
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
        command = commands[idx]
    print(f"Part 1: {accumulator}")

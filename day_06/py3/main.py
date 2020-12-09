
def part_1():
    with open("day_06/input.txt") as f:
        lines = []
        line_str = ""
        for line in f.readlines():
            if line.strip() == "":
                lines.append(set(line_str))
                line_str = ""
            else:
                line_str += line.strip()
        if line_str:
            lines.append(set(line_str))
    return sum((len(line) for line in lines))


print(part_1())

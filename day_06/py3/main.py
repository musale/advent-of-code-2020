# from itertools import zip_longest


# def part_1():
#     with open("day_06/input.txt") as f:
#         lines = []
#         line_str = ""
#         for line in f.readlines():
#             if line.strip() == "":
#                 lines.append(set(line_str))
#                 line_str = ""
#             else:
#                 line_str += line.strip()
#         if line_str:
#             lines.append(set(line_str))
#     return sum((len(line) for line in lines))


# def part_2():
#     with open("day_06/input.txt") as f:
#         lines = []
#         line_str = []
#         for line in f.readlines():
#             if line.strip() == "":
#                 lines.append(line_str)
#                 line_str = []
#             else:
#                 line_str.append([c for c in line if c != "\n"])
#         if line_str:
#             lines.append(line_str)
#     total = 0
#     for line in lines:
#         if len(line) == 1:
#             total += len(set(line.pop()))
#         else:
#             zipped = zip_longest(*line, fillvalue="#")
#             print(list(zipped))
#             for z in zipped:
#                 if len(set(z)) == 1:
#                     total += 1
#     return total


# print(part_1())
# print(part_2())

with open("day_06/input.txt") as f:
    input = f.read().strip().split('\n\n')


def yes_answers(input, fcn):
    for group in input:
        yield len(fcn(*(set(s) for s in group)))


input = [line.split() for line in input]

print("Part 1:", sum(yes_answers(input, set.union)))

print("Part 2:", sum(yes_answers(input, set.intersection)))

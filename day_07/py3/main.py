import re
with open("day_07/input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

checked = []
shiny_rx = r"\d+ shiny gold bag(?:s)?(?:,|.)"

for line in lines:
    if re.search(shiny_rx, line):
        checked.append(line)

for bag in checked:
    bag_name = " ".join(bag.split(" ")[:3])
    for line in lines:
        if bag_name[:-1] in line and line not in checked:
            checked.append(line)
print(len(checked))
# for line in lines:
#     if matches := re.findall(bag_rx, line):
#         for match in matches:
#             fixed = match if match.endswith("s") else match + "s"
#             print(fixed)
#             if fixed == "shiny gold bags":
#                 total += 1
#                 break
#             found = False
#             for l in lines:
#                 if l.startswith(fixed):
#                     if re.search(r"\d+ shiny gold bag", l):
#                         found = True
#                         total += 1
#                         break
#             if found:
#                 break
# print(total)

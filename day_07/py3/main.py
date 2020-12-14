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


# WIP: part 2
gold_bag = None
for line in lines:
    if line.startswith("shiny gold bags"):
        gold_bag = line
        break

bag_rx = r"(\d+)\s(\w+\s\w+\sbag(?:s)?)(?:,|.)"
matches = re.findall(bag_rx, gold_bag)
found = set(matches)
# while (matches):
for match in matches:
    for line in lines:
        if line.startswith(match[1]):
            new_match = re.findall(bag_rx, line)
            for n in new_match:
                found.add(n)
print(found)

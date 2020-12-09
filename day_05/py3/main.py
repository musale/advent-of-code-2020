def part_1():
    file = open('day_05/input.txt', 'r')
    highest_id = 0

    for lineWithOptionNewLine in file:
        line = lineWithOptionNewLine.strip('\n')
        left = 0
        right = 127
        for letter in line[:-3]:
            mid = (left + right) // 2
            if letter == "F":
                right = mid
            else:
                left = mid + 1
        row = left
        left = 0
        right = 7
        for letter in line[-3:]:
            mid = (left + right) // 2
            if letter == "L":
                right = mid
            else:
                left = mid + 1
        col = left
        id = row * 8 + col

        highest_id = max(highest_id, id)

    return highest_id


def part_2():
    file = open('day_05/input.txt', 'r')

    ids = []

    for lineWithOptionNewLine in file:
        line = lineWithOptionNewLine.strip('\n')
        left = 0
        right = 127
        for letter in line[:-3]:
            mid = (left + right) // 2
            if letter == "F":
                right = mid
            else:
                left = mid + 1
        row = left
        left = 0
        right = 7
        for letter in line[-3:]:
            mid = (left + right) // 2
            if letter == "L":
                right = mid
            else:
                left = mid + 1
        ids.append(row * 8 + left)

    sortedIds = sorted(ids)

    for i in range(len(sortedIds) - 1):
        if sortedIds[i] + 2 == sortedIds[i+1]:
            return sortedIds[i] + 1

    return -1


print(part_2())
print(part_1())

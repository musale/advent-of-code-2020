WIN_SIZE = 25


def valid_number(window, number):
    for n in window:
        dif = abs(number-n)
        if n != dif and dif in window:
            return True
    return False


def find_wrong(input):
    window = input[:WIN_SIZE]
    i = 1
    for number in input[WIN_SIZE:]:
        if not valid_number(window, number):
            return number
        else:
            window = input[i:WIN_SIZE+i]
            i += 1
    return False


def find_contiguous(input, wrong):
    for size in range(2, len(input)):
        window = input[:size]
        i = 1
        while i < len(input)-size:
            if sum(window) == wrong:
                return window
            i += 1
            window = input[i:size+i]

    return False


with open("day_09/input.txt", "r") as file:
    input = list(map(int, file.read().strip().splitlines()))

wrong = find_wrong(input)
print("WRONG NUMBER:", wrong)
wrong_set = find_contiguous(input, wrong)
print(min(wrong_set)+max(wrong_set))

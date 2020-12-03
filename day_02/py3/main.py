import re


class Password:
    def __init__(self, min_int, max_int, character, password) -> None:
        self.min_int = min_int
        self.max_int = max_int
        self.character = character
        self.password = password

    def within_min_max(self) -> bool:
        counter = self.password.count(self.character)
        if self.min_int <= counter and self.max_int >= counter:
            return True
        return False


if __name__ == '__main__':
    policies = [re.findall(r"(\d+)-(\d+)\s([a-z]):\s(.*)", n.strip()).pop()
                for n in open("day_02/input.txt").readlines()]

    policies = [Password(int(n[0]), int(n[1]), n[2], n[3]) for n in policies]
    min_max_count = 0
    for policy in policies:
        if policy.within_min_max():
            min_max_count += 1
    print(f"Part 1: {min_max_count}")

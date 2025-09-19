from python_tools import *

def part1(data: list[str]) -> int:
    floor = 0
    for c in data[0]:
        if c == "(": floor += 1
        if c == ")": floor -= 1
    return floor

def part2(data: list[str]) -> int:
    floor = 0
    for i, c in enumerate(data[0]):
        if c == "(": floor += 1
        if c == ")": floor -= 1
        if floor == -1: 
            return i+1
        return -1

if __name__ == "__main__":
    data = read_lines("day01-input.txt")
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))


# from python_tools import *

# def part1(data: list[str]) -> int:
#     return data[0].count("(") - data[0].count(")")

# def part2(data: list[str]) -> int:
#     floor = 0
#     for i, c in enumerate(data[0], 1):  # 1-based index
#         if c == "(":
#             floor += 1
#         elif c == ")":
#             floor -= 1
#         if floor == -1:
#             return i
#     return -1  # just in case

# if __name__ == "__main__":
#     data = read_lines("day01-input.txt")
#     print("Part 1:", part1(data))
#     print("Part 2:", part2(data))

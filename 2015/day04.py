from python_tools import *
import hashlib

def part1(data: list[str]) -> int:
    res = ""
    key = data[0]
    n = 0
    while True:
        candidate = key + str(n)
        h = hashlib.md5(candidate.encode())
        hash_hex = h.hexdigest()
        if hash_hex[:5] == "00000":
            res = n
            break
        n += 1

    return res

def part2(data: list[str]) -> int:
    res = ""
    key = data[0]
    n = 0
    while True:
        candidate = key + str(n)
        h = hashlib.md5(candidate.encode())
        hash_hex = h.hexdigest()
        if hash_hex[:6] == "000000":
            res = n
            break
        n += 1

    return res

if __name__ == "__main__":
    data = read_lines("day04-input.txt")
    print(f"Part1: {part1(data)}")
    print(f"Part2: {part2(data)}")


# from python_tools import *
# import hashlib

# def mine(data: list[str], prefix: str) -> int:
#     key = data[0]
#     n = 0
#     while True:
#         candidate = key + str(n)
#         hash_hex = hashlib.md5(candidate.encode()).hexdigest()
#         if hash_hex.startswith(prefix):
#             return n
#         n += 1

# def part1(data: list[str]) -> int:
#     return mine(data, "00000")

# def part2(data: list[str]) -> int:
#     return mine(data, "000000")

# if __name__ == "__main__":
#     data = read_lines("day04-input.txt")
#     print(f"Part1: {part1(data)}")
#     print(f"Part2: {part2(data)}")

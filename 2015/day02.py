from python_tools import *

# 29x13x26
def part1(datas: list[str]) -> int:
    res = 0
    for data in datas:
        nums = data.split("x")
        l = int(nums[0])
        w = int(nums[1])
        h = int(nums[2])
        sf = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
        res += sf
    
    return res

def part2(datas: list[str]) -> int:
    res = 0
    for data in datas:
        l, w, h = sorted(map(int, data.split("x")))
        ribbon_needed = 2*l + 2*w + l*w*h
        res += ribbon_needed 

    return res

if __name__ == "__main__":
    datas = read_lines("day02-input.txt")
    print("Part1: ", part1(datas))
    print("Part2: ", part2(datas))

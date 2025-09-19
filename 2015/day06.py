from python_tools import *

def part1(data: list[str]) -> int:
    grid = [[0]*1000 for i in range(1000)]

    for words in data:
        instr = words.split()
        if instr[0] == "toggle":
            s1, s2 = map(int, instr[1].split(","))
            e1, e2 = map(int, instr[-1].split(","))
            for r in range(s1,e1+1):
                for c in range(s2, e2+1):
                    if grid[r][c] == 1: grid[r][c] = 0
                    elif grid[r][c] == 0: grid[r][c] = 1
        if instr[1] == 'on': 
            s1, s2 = map(int, instr[2].split(","))
            e1, e2 = map(int, instr[-1].split(","))
            for r in range(s1,e1+1):
                for c in range(s2, e2+1):
                    grid[r][c] = 1
        if instr[1] == 'off':
            s1, s2 = map(int, instr[2].split(","))
            e1, e2 = map(int, instr[-1].split(","))
            for r in range(s1,e1+1):
                for c in range(s2, e2+1):
                    grid[r][c] = 0

    res = 0
    for r in range(1000):
        for c in range(1000):
            res += grid[r][c]
    return res

def part2(data: list[str]) -> int:
    grid = [[0]*1000 for i in range(1000)]

    for words in data:
        instr = words.split()
        if instr[0] == "toggle":
            s1, s2 = map(int, instr[1].split(","))
            e1, e2 = map(int, instr[-1].split(","))
            for r in range(s1,e1+1):
                for c in range(s2, e2+1):
                    grid[r][c] += 2
                    if grid[r][c] < 0:
                        grid[r][c] = 0
        if instr[1] == 'on': 
            s1, s2 = map(int, instr[2].split(","))
            e1, e2 = map(int, instr[-1].split(","))
            for r in range(s1,e1+1):
                for c in range(s2, e2+1):
                    grid[r][c] += 1
        if instr[1] == 'off':
            s1, s2 = map(int, instr[2].split(","))
            e1, e2 = map(int, instr[-1].split(","))
            for r in range(s1,e1+1):
                for c in range(s2, e2+1):
                    grid[r][c] -= 1
                    if grid[r][c] < 0:
                        grid[r][c] = 0

    res = 0
    for r in range(1000):
        for c in range(1000):
            res += grid[r][c]
    return res


if __name__ == "__main__":
    data = read_lines("day06-input.txt")
    print(f"Part1: {part1(data)}")
    print(f"Part2: {part2(data)}")
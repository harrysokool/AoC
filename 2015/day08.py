from python_tools import *

def part1(data: list[str]) -> int:
    sum1 = 0
    sum2 = 0
    for line in data:
        sum1 += len(line)

        newline = line[1:-1]
        i = 0
        while i<len(newline):
            if i < len(newline)-1:
                if newline[i] == "\\" and newline[i+1] == "x":
                    i += 3
                elif newline[i] == "\\" and newline[i+1] != "x":
                    i += 1
            sum2 += 1
            i += 1
            
    return sum1-sum2

def part2(data: list[str]) -> int:
    sum1 = 0
    sum2 = 0
    for line in data:
        sum1 += len(line)

        temp = len(line) + 4
        newline = line[1:-1]
        i = 0
        while i<len(newline):
            if newline[i] == "\"" or newline[i] == "\\":
                temp += 1
            i += 1
        sum2 += temp
            
    return abs(sum1-sum2)


if __name__ == "__main__":
    data = read_lines("day08-input.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 1: {part2(data)}")
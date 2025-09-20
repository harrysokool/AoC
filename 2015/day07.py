from python_tools import *

def part1(data: list[str]):
    hm = {}
    for instrs in data:
        instr = instrs.split()
        if instr[0].isdigit():  # 123 -> x
            val = instr[0]
            dst = instr[-1]
            hm[dst] = val
        elif instr[0] == "NOT": # NOT lk -> ll
            src = instr[1]
            dst = instr[-1]
            hm[dst] = ~src & 0xFFFF
        elif instr[1] == "AND": # af AND ah -> ai
            wire1 = instr[0]
            wire2 = instr[2]
            dst = instr[-1]
            hm[dst] = wire1 & wire2 
        elif instr[1] == "OR": # af OR ah -> ai
            wire1 = instr[0]
            wire2 = instr[2]
            dst = instr[-1]
            hm[dst] = wire1 | wire2 
        elif instr[1] == "LSHIFT": # af LSHIFT 2 -> ai
            wire1 = instr[0]
            n = instr[2]
            dst = instr[-1]
            hm[dst] = wire1 << wire2 
        elif instr[1] == "RSHIFT": # af RSHIFT 2 -> ai
            wire1 = instr[0]
            n = instr[2]
            dst = instr[-1]
            hm[dst] = wire1 >> wire2 
            
    return hm[a]

if __name__ == "__main__":
    data = read_lines("day07-input.txt")
    print(f"Part1: {part1(data)}")
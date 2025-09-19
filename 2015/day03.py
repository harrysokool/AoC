from python_tools import *

def part1(data: list[str]) -> int:
    houses = set([(0, 0)])
    coord = [0, 0]
    for dir in data[0]:
        if dir == ">":  coord[0] += 1
        if dir == "<":  coord[0] -= 1
        if dir == "v":  coord[1] += 1
        if dir == "^":  coord[1] -= 1
        houses.add(tuple(coord))
        
    return len(houses)

def part2(data: list[str]) -> int:
    houses = set([(0, 0)])
    # will only move if index is even
    santa = [0, 0]
    # will only move if index is odd
    robo_santa = [0, 0]
    moves = {">": (1,0), "<": (-1,0), "^": (0,-1), "v": (0,1)}

    
    for i, dir in enumerate(data[0]):
        x, y = moves[dir]
        if i%2 == 0: 
            # santa move
            santa[0] += x
            santa[1] += y
            houses.add(tuple(santa))
        else:
            # robo santa move
            robo_santa[0] += x
            robo_santa[1] += y
            houses.add(tuple(robo_santa))
        
    return len(houses)

if __name__ == "__main__":
    data = read_lines("day03-input.txt")
    print(f"Part1: {part1(data)}")
    print(f"Part2: {part2(data)}")



# def part1(data: list[str]) -> int:
#     moves = {">": (1,0), "<": (-1,0), "^": (0,-1), "v": (0,1)}
#     houses = {(0,0)}
#     x = y = 0
#     for ch in data[0]:
#         dx, dy = moves[ch]
#         x, y = x+dx, y+dy
#         houses.add((x,y))
#     return len(houses)

# def part2(data: list[str]) -> int:
#     moves = {">": (1,0), "<": (-1,0), "^": (0,-1), "v": (0,1)}
#     houses = {(0,0)}
#     santa = (0,0)
#     robo = (0,0)

#     for i, ch in enumerate(data[0]):
#         dx, dy = moves[ch]
#         if i % 2 == 0:  # Santa’s turn
#             santa = (santa[0] + dx, santa[1] + dy)
#             houses.add(santa)
#         else:           # Robo’s turn
#             robo = (robo[0] + dx, robo[1] + dy)
#             houses.add(robo)

#     return len(houses)

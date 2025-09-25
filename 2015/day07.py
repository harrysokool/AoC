from python_tools import *

rules = {}
cache = {}

# populate the rules hashmap
def parse(data: list[str]):
    for line in data:
        expr, target = line.split(" -> ")
        rules[target] = expr.split()

def evaluate(wire: str) -> int:
    # if wire is just a number
    if wire.isdigit():
        return int(wire)
    
    # check if wire in cache
    if wire in cache:
        return cache[wire]
    
    # get the expression from the rules
    expr = rules[wire]

    if len(expr) == 1:
        value = evaluate(expr[0])
    elif "AND" in expr:
        value = evaluate(expr[0]) & evaluate(expr[2])
    elif "OR" in expr:
        value = evaluate(expr[0]) | evaluate(expr[2])
    elif "LSHIFT" in expr:
        value = evaluate(expr[0]) << int(evaluate(expr[2]))
    elif "RSHIFT" in expr:
        value = evaluate(expr[0]) >> int(evaluate(expr[2]))
    elif "NOT" in expr:
        value = ~evaluate(expr[1]) & 0xFFFF

    cache[wire] = value
    return value
    

def part1(data: list[str]) -> int:
    parse(data)
    return evaluate("a")

def part2(data: list[str]) -> int:
    parse(data)
    cache.clear()
    # overwrite b with the value you found in Part 1 (example: 956)
    rules["b"] = [str(956)]
    return evaluate("a")

if __name__ == "__main__":
    data = read_lines("day07-input.txt")
    print(f"Part1: {part1(data)}")
    print(f"Part1: {part2(data)}")

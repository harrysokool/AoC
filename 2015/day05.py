from python_tools import *

def hasDouble(word: str) -> bool:
    for i in range(len(word)):
        if i>0 and word[i] == word[i-1]:
            return True

    return False

def has_forbidden(word: str) -> bool:
    return any(bad in word for bad in ["ab", "cd", "pq", "xy"])

def part1(data: list[str]) -> int:
    count = 0
    for word in data:
        if sum(1 for c in word if c in "aeiou") >= 3:
            if hasDouble(word):
                if not has_forbidden(word):
                    count += 1

    return count

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
def req1(word: str) -> bool:
    for i in range(len(word)-2):
        substring = word[i: i+2]
        if substring in word[i+2:]:
            return True
        
    return False

# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
def req2(word: str) -> bool:
    return any(word[i] == word[i+2] for i in range(len(word)-2))

def part2(data: list[str]) -> int:
    count = 0
    for word in data:
        if len(word) <= 2: return False
        if req1(word) and req2(word):
            count += 1

    return count

if __name__ == "__main__":
    data = read_lines("day05-input.txt")
    print(f"Part1: {part1(data)}")
    print(f"Part2: {part2(data)}")
    test = "hello"

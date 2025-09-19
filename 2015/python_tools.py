from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
import re
import math

# --------------------------
# File Handling
# --------------------------
def read_lines(filename: str) -> list[str]:
    """Read file into a list of stripped lines."""
    with open(filename) as f:
        return [line.strip() for line in f]

def read_ints(filename: str) -> list[int]:
    """Read file where each line is an integer."""
    return [int(x) for x in read_lines(filename)]

def read_chunks(filename: str, sep="\n\n") -> list[str]:
    """Read file and split by blank lines (useful for grouped input)."""
    with open(filename) as f:
        return f.read().strip().split(sep)

# --------------------------
# Grid Utilities
# --------------------------
DIRS4 = [(1,0), (-1,0), (0,1), (0,-1)]          # 4-directional
DIRS8 = [(1,0), (-1,0), (0,1), (0,-1),
         (1,1), (1,-1), (-1,1), (-1,-1)]        # 8-directional

def in_bounds(r, c, rows, cols) -> bool:
    return 0 <= r < rows and 0 <= c < cols

def neighbors4(r, c, rows, cols):
    for dr, dc in DIRS4:
        nr, nc = r+dr, c+dc
        if in_bounds(nr, nc, rows, cols):
            yield nr, nc

def neighbors8(r, c, rows, cols):
    for dr, dc in DIRS8:
        nr, nc = r+dr, c+dc
        if in_bounds(nr, nc, rows, cols):
            yield nr, nc

# --------------------------
# Graph / Search Helpers
# --------------------------
def bfs(start, get_neighbors):
    """Generic BFS. get_neighbors(node) should yield neighbors."""
    q = deque([start])
    visited = {start: 0}  # node -> distance
    while q:
        cur = q.popleft()
        for nxt in get_neighbors(cur):
            if nxt not in visited:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
    return visited  # contains all reachable nodes and dist

def dfs(start, get_neighbors, visited=None):
    """Generic DFS. Returns set of visited nodes."""
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in get_neighbors(start):
        if nxt not in visited:
            dfs(nxt, get_neighbors, visited)
    return visited

# --------------------------
# Math / Misc
# --------------------------
def manhattan(p1, p2) -> int:
    """Manhattan distance between 2 points."""
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def lcm(a, b) -> int:
    """Least common multiple."""
    return abs(a*b) // math.gcd(a, b)

def flatten(lst):
    """Flatten a list of lists."""
    return [x for sub in lst for x in sub]

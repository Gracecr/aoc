from functools import cache

from aoc import util as u

D = u.get_data().split("\n\n")
PATTERNS = set(D[0].split(", "))


@cache
def num_ways(design: str) -> int:
    if design == "":
        return 1
    n = 0
    for pattern in PATTERNS:
        if design.startswith(pattern):
            n += num_ways(design[len(pattern) :])
    return n


p1 = 0
p2 = 0
for i, design in enumerate(D[1].splitlines()):
    n = num_ways(design)
    if n:
        p1 += 1
        p2 += n

print(p1)
print(p2)

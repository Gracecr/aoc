from functools import cache

from aoc import util as u

PATTERNS, DESIGNS = u.get_data().split("\n\n")
PATTERNS = set(PATTERNS.split(", "))
DESIGNS = DESIGNS.splitlines()


@cache
def num_ways(design: str) -> int:
    if design == "":
        return 1
    return sum(num_ways(design[len(p) :]) for p in PATTERNS if design.startswith(p))


n_different_ways = [num_ways(design) for design in DESIGNS]

print(sum(1 for n_ways in n_different_ways if n_ways))
print(sum(n_different_ways))

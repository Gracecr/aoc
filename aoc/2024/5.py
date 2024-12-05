from collections import defaultdict
from functools import cmp_to_key

from aoc import util as u

D = u.get_data().splitlines()


RULES = defaultdict(set)
p1 = 0
p2 = 0
for line in D:
    if "|" in line:
        a, b = line.split("|")
        RULES[a].add(b)
    if "," in line:
        pages = line.split(",")
        sorted_pages = sorted(
            pages, key=cmp_to_key(lambda a, b: -1 if b in RULES[a] else 1)
        )
        if pages == sorted_pages:
            p1 += pages[len(pages) // 2]
        else:
            p2 += sorted_pages[len(sorted_pages) // 2]

print(p1)
print(p2)

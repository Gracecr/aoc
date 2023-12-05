from aoc.util import *

d = get_data().splitlines()

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

ntrees_lst = []
for x, y in slopes:
    r = y
    c = x
    ntrees = 0
    while r < len(d):
        if d[r][c % len(d[r])] == "#":
            ntrees += 1
        r += y
        c += x
    ntrees_lst.append(ntrees)
submit(functools.reduce(operator.mul, ntrees_lst))
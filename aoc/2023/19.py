from aoc.util import *

D = get_data().split("\n\n")[0].splitlines()

G: dict[str, tuple[list, tuple]] = {}

for line in D:
    name, rest = line[:-1].split("{")
    conditions = rest.split(",")
    G[name] = ([], conditions.pop())
    for condition in conditions:
        cond, f = condition.split(":")
        var, op = cond[0:2]
        n = int(cond[2:])
        G[name][0].append((var, op, n, f))


def count(ranges: dict[str, tuple[int, int]], rule_name: str = "in"):
    if rule_name == "R":
        return 0

    if rule_name == "A":
        v = 1
        for lo, hi in ranges.values():
            v *= hi - lo + 1
        return v

    total = 0
    rules, fallback = G[rule_name]
    for var, op, n, f in rules:
        lo, hi = ranges[var]
        if op == "<":
            T = (lo, min(n - 1, hi))
            F = (max(n, lo), hi)
        else:
            T = (max(n + 1, lo), hi)
            F = (lo, min(n, hi))

        if T[0] <= T[1]:
            ranges_copy = dict(ranges)
            ranges_copy[var] = T
            total += count(ranges_copy, f)

        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[var] = F
        else:
            break
    else:
        total += count(ranges, fallback)

    return total


print(count({l: (1, 4000) for l in "xmas"}))

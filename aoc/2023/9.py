from aoc.util import *

D = get_data().splitlines()


def sub_list(l):
    new_l = []
    for a, b in zip(l, l[1:]):
        new_l.append(b - a)
    return new_l


V = []
for line in D:
    data = [int(n) for n in line.split()]
    hist = [list(data)]
    while any(h != 0 for h in hist[-1]):
        hist.append(sub_list(hist[-1]))

    val = 0
    for r in hist[::-1]:
        val = r[0] - val

    V.append(val)

print(sum(V))
submit(sum(V))

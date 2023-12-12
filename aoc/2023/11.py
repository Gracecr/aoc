from aoc.util import *

D = get_data().splitlines()
# D = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....""".splitlines()


# EXPAND_RATE = 1
EXPAND_RATE = 1000000 - 1

G = list()
# Add initial pos
for r, line in enumerate(D):
    for c, char in enumerate(line):
        if char == "#":
            G.append((r,c))
print(G)


# Adjust row
num_shifts = -1
for r, line in enumerate(D):
    if "#" not in line:
        num_shifts += 1
        new_set = list()
        for g in G:
            if g[0] > r + num_shifts * EXPAND_RATE:
                new_set.append((g[0] + EXPAND_RATE, g[1]))
            else:
                new_set.append(g)
        G = new_set
print(G)

#Adjust Column
num_shifts = -1
for c, line in enumerate(zip(*D)):
    if "#" not in line:
        num_shifts += 1
        new_set = list()
        for g in G:
            if g[1] > c + num_shifts * EXPAND_RATE:
                new_set.append((g[0], g[1] + EXPAND_RATE))
            else:
                new_set.append(g)
        G = new_set
print(G)
acc = 0
for g1, g2 in itertools.combinations(G, 2):
    acc += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

submit(acc)

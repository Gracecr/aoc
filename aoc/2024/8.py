import itertools
from collections import defaultdict

from aoc import util as u

D = u.get_data().splitlines()
B = u.get_bounds(D)
G = defaultdict(list)

part2 = 0
for r, line in enumerate(D):
    for c, ch in enumerate(line):
        if ch != ".":
            G[ch].append((r, c))

P1_ANTINODES = set()
P2_ANTINODES = set()

for ch in G:
    for p1, p2 in itertools.combinations(G[ch], 2):
        p1_diff = (p1[0] - p2[0], p1[1] - p2[1])
        p2_diff = (p2[0] - p1[0], p2[1] - p1[1])

        for pos in (u.addt(p1, p1_diff), u.addt(p2, p2_diff)):
            if u.is_in_bounds(B, pos):
                P1_ANTINODES.add(pos)

        pos = p1
        while u.is_in_bounds(B, pos):
            P2_ANTINODES.add(pos)
            pos = u.addt(pos, p1_diff)
        pos = p2
        while u.is_in_bounds(B, pos):
            P2_ANTINODES.add(pos)
            pos = u.addt(pos, p2_diff)

part1 = len(P1_ANTINODES)
part2 = len(P2_ANTINODES)
print(part1)
print(part2)

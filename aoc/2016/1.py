from aoc.util import *

d = [d for d in get_data().split(", ")]
dir = 0
loc = [0, 0]
visited = {tuple(loc)}
for cmd in d:
    if cmd[0] == "R":
        dir = (dir + 1) % 4
    if cmd[0] == "L":
        dir = (dir - 1) % 4
    dist = int(cmd[1:])
    for _ in range(1, dist + 1):
        if dir == 0:
            loc[0] += 1
        if dir == 1:
            loc[1] += 1
        if dir == 2:
            loc[0] -= 1
        if dir == 3:
            loc[1] -= 1
        if tuple(loc) in visited:
            print(loc[0] + loc[1])
            exit()
        visited.add(tuple(loc))
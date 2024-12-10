from collections import deque

from aoc import util as u

D = u.get_data().splitlines()
V = u.get_vectors(2)
B = u.get_bounds(D)

p1 = 0
p2 = 0


TRAIL_HEADS = []

for r, line in enumerate(D):
    for c, ch in enumerate(line):
        if ch == "0":
            TRAIL_HEADS.append((r, c))


def bfs(pos: tuple[int, int], part2: bool = False) -> int:
    num_9_reachable = 0
    visited = set()
    q = deque([pos])
    while q:
        n = q.popleft()
        n_v = int(D[n[0]][n[1]])
        if n_v == 9:
            num_9_reachable += 1

        for neigh in u.get_neighbors(n, V, B):
            if part2 and neigh in visited:
                continue
            if n_v - int(D[neigh[0]][neigh[1]]) == -1:
                if part2:
                    visited.add(neigh)
                q.append(neigh)
    return num_9_reachable


for trail_head in TRAIL_HEADS:
    p1 += bfs(trail_head)
    p2 += bfs(trail_head, part2=True)

print(p1)
print(p2)

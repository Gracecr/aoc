import heapq as hq
from collections import defaultdict, deque

from aoc import util as u

D = u.get_data().splitlines()
V = u.get_vectors(2)
Q = deque()

p1 = 0
p2 = 0

start = None
end = None
direction = (0, 1)
for r, line in enumerate(D):
    for c, ch in enumerate(line):
        if ch == "S":
            start = (r, c)
        elif ch == "E":
            end = (r, c)

PREV = defaultdict(set)


def dijkstra(start):
    distances = defaultdict(lambda: 10**9)
    heap = [(0, start)]

    while heap:
        dist, node = hq.heappop(heap)
        if node in distances and dist > distances[node]:
            continue
        pos, direction = node
        distances[node] = dist
        for neighbor, weight in [
            ((u.addt(pos, direction), direction), 1),
            ((pos, (-direction[1], direction[0])), 1000),
            ((pos, (direction[1], -direction[0])), 1000),
        ]:
            n_pos, n_direction = neighbor
            if neighbor not in distances and D[n_pos[0]][n_pos[1]] != "#":
                hq.heappush(heap, (dist + weight, neighbor))
                PREV[neighbor].add(node)

    return distances


def get_shortest_paths(start, end):
    ends = [(end, tuple(v)) for v in V]
    dists = dijkstra(start)
    min_dist = min(dists[d] for d in dists if d[0] == end)
    shortest_paths = []
    for end in ends:
        if dists[end] == min_dist:
            shortest_paths.append(end)

    poses_in_path = set()
    for path in shortest_paths:
        poses_in_path.update(_get_shortest_paths(path, start))

    return poses_in_path


def _get_shortest_paths(start, end):
    shortest_paths = set([start[0]])
    for path in PREV[start]:
        shortest_paths.update(_get_shortest_paths(path, end))
    return shortest_paths


shortest_paths = get_shortest_paths((start, (0, 1)), end)

# shortest = min(dists[d] for d in dists if d[0] == end)
# # print(dists)
# print(min(dists[d] for d in dists if d[0] == end))
# print(p1)


for r, line in enumerate(D):
    for c, ch in enumerate(line):
        if (r, c) in shortest_paths:
            print("O", end="")
        else:
            print(ch, end="")
    print()

print(len(shortest_paths))

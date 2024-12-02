import heapq

from aoc.util import *

D = get_data().splitlines()

HMAP = defaultdict(lambda: 0)
G = nx.Graph()
G2 = nx.Graph()
B = get_bounds(D)
VEC = get_vectors(2)

for r, line in enumerate(D):
    for c, ch in enumerate(line):
        for n in get_neighbors((r, c), VEC, B):
            G.add_edge((r, c), n, weight=int(ch))

# for node in G.nodes:
#     for end, path in nx.single_source_dijkstra_path(G, node, cutoff=4).items():
#         if abs(node[0] - end[0]) + abs(node[1] - end[1]) == 3:
#             G2.add_edge(node, path[-1], weight=nx.path_weight(G, path, "weight"))


def dj(source):
    dists = defaultdict(lambda: 999999999)
    prev = defaultdict(lambda: None)
    q = [(0, source, (1, 0), 0)]
    dists[q[0]] = 0
    vis = set()
    while q:
        u = heapq.heappop(q)

        if u in vis:
            continue
        vis.add(u)

        dist, node, direction, steps = u
        for vec in VEC:
            cur_steps = steps
            vec = tuple(vec)
            if addt(vec, direction) == (0, 0):
                continue

            next_node = addt(node, vec)
            if not is_in_bounds(B, next_node):
                continue

            if tuple(vec) == tuple(direction):
                if steps + 1 > 10:
                    continue
                cur_steps += 1
            elif cur_steps < 4:
                continue
            else:
                cur_steps = 1

            new_dist = dist + int(D[node[0]][node[1]])
            if new_dist < dists[(next_node, vec, cur_steps)]:
                dists[(next_node, vec, cur_steps)] = new_dist
                v = (new_dist, next_node, vec, cur_steps)
                heapq.heappush(q, v)
                prev[v] = u

    min_dist = 99999999999
    end_node = None
    for n, d in dists.items():
        if n[0] == (len(D) - 1, len(D[0]) - 1) and d < min_dist:
            min_dist = d
            end_node = (d, *n)

    S = []
    u = end_node
    while u:
        S.insert(0, u)
        u = prev[u]

    path = S
    m = {
        (0, 1): ">",
        (0, -1): "<",
        (1, 0): "v",
        (-1, 0): "^",
    }
    for r, line in enumerate(D):
        for c, ch in enumerate(line):
            if any((r, c) == p[1] for p in path):
                print(m[next(p[2] for p in path if (r, c) == p[1])], end="")
            else:
                print(ch, end="")
        print()

    acc = 0
    for p in path[1:]:
        acc += int(D[p[1][0]][p[1][1]])
    print(acc)


dj((0, 0))

# path = nx.shortest_path(G2, (0, 0), (len(D) - 1, len(D[0]) - 1), "weight")
# direction = (-1, -1)
# direction_count = 0
# for path in paths:
#     for i, n in enumerate(path):
#         if i + 1 < len(path):
#             new_direction = addt(n, path[i + 1])
#             if new_direction == direction:
#                 direction_count += 1
#                 if direction_count > 3:
#                     break
#             else:
#                 direction = new_direction
#                 direction_count = 0
#     if direction_count < 3:
#         print(nx.path_weight(G, path, "weight"))
#         break

# path = nx.dijkstra_path(G2, (0, 0), (len(D) - 1, len(D[0]) - 1))
# print(nx.path_weight(G2, path, "weight"))

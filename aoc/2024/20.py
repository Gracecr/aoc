from collections.abc import Iterator

from aoc import util as u

D = u.get_data().splitlines()
V = u.get_vectors(2)
B = u.get_bounds(D)
G = u.nx.Graph()


for cheat, line in enumerate(D):
    for c, ch in enumerate(line):
        if ch == "S":
            start = (cheat, c)
        elif ch == "E":
            end = (cheat, c)
        elif ch == "#":
            continue
        for neigh in u.get_neighbors((cheat, c), V, B):
            if D[neigh[0]][neigh[1]] != "#":
                G.add_edge((cheat, c), neigh)


def cheats(pos: tuple[int, int], length: int) -> Iterator[tuple[int, int]]:
    for dist in range(1, length + 1):
        for offset in range(dist):
            inv_offset = dist - offset
            n1 = pos[0] + offset, pos[1] + inv_offset
            n2 = pos[0] + inv_offset, pos[1] - offset
            n3 = pos[0] - offset, pos[1] - inv_offset
            n4 = pos[0] - inv_offset, pos[1] + offset
            for n in n1, n2, n3, n4:
                if u.is_in_bounds(B, n) and D[n[0]][n[1]] != "#":
                    yield n


def num_cheats(cheat_len: int, min_saved: int = 100) -> int:
    n = 0
    for node in G.nodes:
        for cheat in cheats(node, cheat_len):
            dist = abs(node[0] - cheat[0]) + abs(node[1] - cheat[1])
            if DIST_D[node] - (DIST_D[cheat] + dist) >= min_saved:
                n += 1
    return n


DIST_D = u.nx.shortest_path_length(G, target=end)

print(num_cheats(2))
print(num_cheats(20))

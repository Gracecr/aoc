from aoc import util as u

D = u.get_data().splitlines()
G = u.nx.Graph()
V = u.get_vectors(2)
R = 71
C = 71
B = ((0, R), (0, C))
BLOCKS = set()
TOTAL = 1024

for i, d in enumerate(D):
    if i >= TOTAL:
        break
    BLOCKS.add(tuple(map(int, d.split(","))))


for r in range(R):
    for c in range(C):
        if (r, c) in BLOCKS:
            continue
        for neigh in u.get_neighbors((r, c), V, B):
            if neigh not in BLOCKS:
                G.add_edge((r, c), neigh)


print(u.nx.shortest_path_length(G, (0, 0), (R - 1, C - 1)))

for d in D[TOTAL:]:
    G.remove_node(tuple(map(int, d.split(","))))
    if not u.nx.has_path(G, (0, 0), (R - 1, C - 1)):
        print(d)
        break

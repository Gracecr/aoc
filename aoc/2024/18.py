from aoc import util as u

D = u.get_data().splitlines()
G = u.nx.Graph()
V = u.get_vectors(2)
R = 71
C = 71
B = ((0, R), (0, C))
P1 = 1024


for r in range(R):
    for c in range(C):
        for neigh in u.get_neighbors((r, c), V, B):
            G.add_edge((r, c), neigh)


for i, d in enumerate(D):
    G.remove_node(tuple(map(int, d.split(","))))
    if i == P1:
        print(u.nx.shortest_path_length(G, (0, 0), (R - 1, C - 1)))

    if not u.nx.has_path(G, (0, 0), (R - 1, C - 1)):
        print(d)
        break

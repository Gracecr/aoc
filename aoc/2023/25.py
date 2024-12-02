from aoc.util import *

D = get_data().splitlines()
G = nx.Graph()

for line in D:
    node, children = line.split(":")
    for child in children.split():
        G.add_edge(node, child)

# print(nx.minimum_edge_cut(G))
G.remove_edges_from(nx.minimum_edge_cut(G))
# print(len(list(nx.connected_components(G))))

print(np.prod([len(c) for c in nx.connected_components(G)]))

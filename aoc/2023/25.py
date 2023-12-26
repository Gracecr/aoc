from aoc.util import *

D = get_data().splitlines()
# D = """jqt: rhn xhk nvd
# rsh: frs pzl lsr
# xhk: hfx
# cmg: qnr nvd lhk bvb
# rhn: xhk bvb hfx
# bvb: xhk hfx
# pzl: lsr hfx nvd
# qnr: nvd
# ntq: jqt hfx bvb xhk
# nvd: lhk
# lsr: lhk
# rzs: qnr cmg lsr rsh
# frs: qnr lhk lsr""".splitlines()
G = nx.Graph()

for line in D:
    node, children = line.split(":")
    for child in children.split():
        G.add_edge(node, child)

# print(nx.minimum_edge_cut(G))
G.remove_edges_from(nx.minimum_edge_cut(G))
# print(len(list(nx.connected_components(G))))

print(np.prod([len(c) for c in nx.connected_components(G)]))

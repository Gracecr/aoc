from aoc.util import *

D = get_data().splitlines()
G = nx.DiGraph()

nodes = []
edges = []
d = D[0]
for line in D[2:]:
    node, rest = line.split(" = ")
    rest = rest.replace("(", "")
    rest = rest.replace(")", "")
    nodes.append(node)
    edges.append(rest.split(", "))

for node, edges in zip(nodes, edges):
    G.add_node(node)
    for edge in edges:
        G.add_edge(node, edge)

# cur = "AAA"
steps = 0
# while cur != "ZZZ":
#     for l in d:
#         print(cur, list(G.neighbors(cur)))
#         if l == "L":
#             cur = list(G.neighbors(cur))[0]
#         if l == "R":
#             cur = list(G.neighbors(cur))[-1]
#         steps += 1
#         if cur == "ZZZ":
#             break

cur_nodes = [n for n in G.nodes if n[-1] == "A"]
seqs = [list() for _ in range(len(cur_nodes))]
seqs_ = [list() for _ in range(len(cur_nodes))]
offsets = [-1 for _ in range(len(cur_nodes))]

while any(sl == -1 for sl in offsets):
    for j, l in enumerate(d):
        for i, cur in enumerate(cur_nodes):
            if offsets[i] != -1:
                continue
            if l == "L":
                cur = list(G.neighbors(cur))[0]
            if l == "R":
                cur = list(G.neighbors(cur))[-1]
            cur_nodes[i] = cur
            if (cur, j) in seqs[i]:
                seqs_[i] = [a[0] for a in seqs[i][seqs[i].index((cur, j)) :]]
            else:
                seqs[i].add((cur, j))
        # print(cur_nodes)
        steps += 1

seq_lengths = [len(s) for s in seqs_]
pos_of_zs = []
for s in seqs_:
    for i, c in enumerate(s):
        if c.endswith("Z"):
            pos_of_zs.append(i)

# print(pos_of_zs)
print(seq_lengths)
# print(seqs_)
# print(seqs)

lcm = math.lcm(*seq_lengths)
print(lcm)

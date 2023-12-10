from aoc.util import *

D = get_data().splitlines()
# D = """FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L""".splitlines()
# D.insert(0, "." * len(D[0]))
# D.append("." * len(D[0]))
# for i in range(len(D)):
#     D[i] = "." + D[i] + "."


V = get_vectors(2)
Vs = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "S": V,
    ".": []
}
G = nx.DiGraph()
B = get_bounds(D)

start = (0, 0)

for r, line in enumerate(D):
    for c, ch in enumerate(line):
        if ch == "S":
            start = (r, c)

vis = set()

q = set([start])
while q:
    pos = q.pop()
    # print(pos, D[pos[0]][pos[1]])
    vis.add(pos)
    cur = D[pos[0]][pos[1]]

    for n in get_neighbors(pos, Vs[cur], B):
        cur_n = D[n[0]][n[1]]
        if cur_n in ("S", "."):
            continue
        # if cur == "|" and cur_n == "-":
        #     continue
        # if cur == "-" and cur_n == "|":
            # continue
        G.add_edge(pos, n)
        if n not in vis:
            q.add(n)


# P2 Flood fill
"""Flood-fill (node):
  1. Set Q to the empty queue or stack.
  2. Add node to the end of Q.
  3. While Q is not empty:
  4.   Set n equal to the first element of Q.
  5.   Remove first element from Q.
  6.   If n is Inside:
         Set the n
         Add the node to the west of n to the end of Q.
         Add the node to the east of n to the end of Q.
         Add the node to the north of n to the end of Q.
         Add the node to the south of n to the end of Q.
  7. Continue looping until Q is exhausted.
  8. Return."""

# Q = set([(0,0)])
# OUTSIDE = set()
# while Q:
#     n = Q.pop()
#     OUTSIDE.add(n)
#     for neighbor in get_neighbors(n, V, B):
#         if neighbor not in OUTSIDE and neighbor not in vis:
#             Q.add(neighbor)

# # P2 BFS
# """ 1  procedure BFS(G, root) is
#  2      let Q be a queue
#  3      label root as explored
#  4      Q.enqueue(root)
#  5      while Q is not empty do
#  6          v := Q.dequeue()
#  7          if v is the goal then
#  8              return v
#  9          for all edges from v to w in G.adjacentEdges(v) do
# 10              if w is not labeled as explored then
# 11                  label w as explored
# 12                  w.parent := v
# 13                  Q.enqueue(w)"""

# Q = set((0, 0))
# EXPLORED = set()

inside = set()
for r, line in enumerate(D):
    for c, ch in enumerate(line):
        cur = (r,c)
        if cur not in vis:
            num_verts = 0
            for c2, ch in enumerate(D[r][:c]):
                if (r, c2) in vis and ch in "|JLS":
                    num_verts += 1
            if num_verts % 2 == 1:
                inside.add(cur)

# print(max(nx.shortest_path_length(G, start).values()))

new_D = []

for r, line in enumerate(D):
    new_D.append("")
    for c, ch in enumerate(line):
        if (r,c) in vis:
            new_D[-1] += "."
        
        elif (r,c) in inside:
            new_D[-1] += "I"
        
        else:
            new_D[-1] += "O"

for line in new_D:
    print(line)

# print((6, 0) in vis)
# print((6, 0) in OUTSIDE)

# print(OUTSIDE)
print(len(vis))
# print((len(D) * len(D[0])) - len(vis.union(OUTSIDE)))
submit(len(inside))
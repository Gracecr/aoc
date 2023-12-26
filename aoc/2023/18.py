from aoc.util import *

D = get_data().splitlines()
# D = """R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)""".splitlines()
V = {
    "0": (0, 1),
    "2": (0, -1),
    "3": (-1, 0),
    "1": (1, 0),
}
M = defaultdict(lambda: ".")
VERTS = []
pos = (0, 0)

num_walls = 0

for line in D:
    # direction, count, color = line.split()
    _, _, color = line.split()
    direction = color[-2]
    count = int(color[2:-2], base=16)
    pos = addt(pos, (V[direction][0] * count, V[direction][1] * count))
    VERTS.append(pos)
    num_walls += count
    # for _ in range(int(count)):
    #     pos = addt(V[direction], pos)
    #     M[pos] = "#"

area = 0
n = len(VERTS)
for i in range(n):
    j = (i + 1) % n
    area += VERTS[i][0] * VERTS[j][1]
    area -= VERTS[j][0] * VERTS[i][1]
area = abs(area) / 2
submit(area + num_walls / 2 + 1)

# num_walls = len(M)

# max_r = 0
# min_r = 9999
# max_c = 0
# min_c = 9999
# for pos in M:
#     if pos[0] > max_r:
#         max_r = pos[0]
#     if pos[1] > max_c:
#         max_c = pos[1]
#     if pos[0] < min_r:
#         min_r = pos[0]
#     if pos[1] < min_c:
#         min_c = pos[1]

# VIS = set()
# Q = [(1, 1)]
# VIS.add(Q[0])
# while Q:
#     v = Q.pop()
#     for n in get_neighbors(v, V.values(), [(min_r, max_r + 1), (min_c, max_c + 1)]):
#         if n not in VIS and M[n] == ".":
#             VIS.add(n)
#             Q.append(n)

# submit(len(VIS) + num_walls)

# # acc = 0
# # for r in range(min_r, max_r + 1):
# #     s = 0
# #     trench_count = 0
# #     for c in range(min_c, max_c + 1):
# #         printed = False
# #         if M[(r, c)] == "#":
# #             s += 1
# #             print("#", end="")
# #             printed = True

# #         if M[(r, c)] == "#" and M[(r, c + 1)] != "#":
# #             trench_count += 1
# #             # if r == 6:
# #             #     print(c)

# #         elif M[(r, c)] == "." and trench_count % 2 == 1:
# #             s += 1
# #             print("#", end="")
# #             printed = True

# #         if not printed:
# #             print(".", end="")

# #     print()
# #     acc += s

# print(acc)

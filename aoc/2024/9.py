from aoc import util as u

D = u.get_data()
SPACE = []
FILLED_SPACES = []
FREE_SPACES = []

p1 = 0
p2 = 0
id_num = 0
if len(D) % 2 != 0:
    D += "0"
for size, free_size in zip(D[::2], D[1::2]):
    FILLED_SPACES.append([len(SPACE), int(size)])
    SPACE.extend([id_num] * int(size))
    FREE_SPACES.append([len(SPACE), int(free_size)])
    SPACE.extend(["."] * int(free_size))
    id_num += 1

for filled_space in FILLED_SPACES[::-1]:
    for free_space in FREE_SPACES:
        if free_space[0] > filled_space[0]:
            break
        if filled_space[1] > free_space[1]:
            continue
        filled_space[0] = free_space[0]
        free_space[1] -= filled_space[1]
        free_space[0] += filled_space[1]


for i, space in enumerate(FILLED_SPACES):
    for j in range(space[1]):
        p2 += (space[0] + j) * i

# x = 0
# y = len(SPACE) - 1
# while y > x:
#     if SPACE[y] == ".":
#         y -= 1
#         continue
#     if SPACE[x] != ".":
#         x += 1
#         continue
#     SPACE[x], SPACE[y] = SPACE[y], SPACE[x]
#     x += 1
#     y -= 1


# for i, v in enumerate(SPACE):
#     if v != ".":
#         p1 += v * i
#         print(i, v, v * i)

# print(p1)
# for i, space in enumerate(FILLED_SPACES):
#     for j in range(space[0], space[0] + space[1]):
#         SPACE[j] = i
# print("".join(str(s) for s in SPACE))
print(p2)

from dataclasses import dataclass

from aoc import util as u


@dataclass
class Block:
    index: int
    size: int


D = u.get_data()
if len(D) % 2 != 0:
    # Assume free space size of 0 at the end if not specified
    D += "0"

SPACE = []
FILLED_SPACES: list[Block] = []
FREE_SPACES: list[Block] = []


p1 = 0
p2 = 0

for id_num, (size, free_size) in enumerate(zip(D[::2], D[1::2])):
    FILLED_SPACES.append(Block(len(SPACE), int(size)))
    SPACE.extend([id_num] * int(size))
    FREE_SPACES.append(Block(len(SPACE), int(free_size)))
    SPACE.extend(["."] * int(free_size))

for filled_space in FILLED_SPACES[::-1]:
    for free_space in FREE_SPACES:
        if free_space.index > filled_space.index:
            break
        if filled_space.size > free_space.size:
            continue
        filled_space.index = free_space.index
        free_space.size -= filled_space.size
        free_space.index += filled_space.size


for id_num, space in enumerate(FILLED_SPACES):
    for i in range(space.size):
        p2 += (space.index + i) * id_num

x = 0
y = len(SPACE) - 1
while y > x:
    if SPACE[y] == ".":
        y -= 1
        continue
    if SPACE[x] != ".":
        x += 1
        continue
    SPACE[x], SPACE[y] = SPACE[y], SPACE[x]
    x += 1
    y -= 1


for i, v in enumerate(SPACE):
    if v != ".":
        p1 += v * i

print(p1)
print(p2)

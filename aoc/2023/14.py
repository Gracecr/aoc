from aoc.util import *

D = [list(l) for l in get_data().splitlines()]

# north, then west, then south, then east
cycles = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# for r, line in enumerate(D):
#     for c, char in enumerate(line):
#         if char == "O":
#             cur_r = r
#             while cur_r > 0 and D[cur_r - 1][c] == ".":
#                 print(r, cur_r, ".")
#                 D[cur_r][c] = "."
#                 cur_r -= 1
#             print(r, cur_r, "O")
#             D[cur_r][c] = "O"


@functools.cache
def cycle(data: tuple[tuple[str]], cycle: tuple[int, int]):
    d = [list(l) for l in data]
    for r, line in enumerate(d):
        r_ = len(d) - r - 1 if cycle[0] > 0 else r
        for c, char in enumerate(line):
            c_ = len(line) - c - 1 if cycle[1] > 0 else c
            if d[r_][c_] == "O":
                prev_pos = (r_, c_)
                next_pos = addt((r_, c_), cycle)
                while (
                    0 <= next_pos[0] < len(d)
                    and 0 <= next_pos[1] < len(d[0])
                    and d[next_pos[0]][next_pos[1]] == "."
                ):
                    d[next_pos[0]][next_pos[1]] = "O"
                    d[prev_pos[0]][prev_pos[1]] = "."
                    next_pos = addt(next_pos, cycle)
                    prev_pos = addt(prev_pos, cycle)
    return tuple(tuple(l) for l in d)


def calc_load(d):
    load = 0
    for r, line in enumerate(d):
        for c, char in enumerate(line):
            if char == "O":
                load += len(d) - r
    return load


def isin(pattern, sequence):
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i : i + len(pattern)] == pattern:
            return i
    return -1


cur_D = tuple(tuple(d) for d in D)
loads = []
N = int(1000000000 / 100000)
valid_loads = set()
for i in range(N):
    if i % (N / 100_000) == 0:
        print(i / N * 100)

    for c in cycles:
        cur_D = cycle(cur_D, c)

    loads.append(calc_load(cur_D))
    if i > 1000:
        valid_loads.add(loads[-1])
        # for r, line in enumerate(cur_D):
        #     print("".join(line))
        # print()
print(valid_loads)
for seq_len in range(1000):
    if all(loads[1000] == a for a in loads[1000::seq_len]):
        print(seq_len)
# seq = loads[N - 10000:]
# offset = isin(seq, loads)
# print(offset)
# print(seq[(1000000000 + offset) % len(seq)])
# print(seq == loads[offset:len(seq)])

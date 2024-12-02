from copy import deepcopy

from aoc.util import *

D = get_data().splitlines()
B = {}
B_POS = defaultdict(list)
MIN_Z = {}

for i, line in enumerate(D):
    label = i
    s, e = line.split("~")
    s = [int(i) for i in s.split(",")]
    e = [int(i) for i in e.split(",")]
    for d, (start, end) in enumerate(zip(s, e)):
        if start == end:
            continue
        for v in range(start, end + 1):
            s_copy = list(s)
            s_copy[d] = v
            B[tuple(s_copy)] = label
            B_POS[label].append(tuple(s_copy))
    if s == e:
        B[tuple(s)] = label
        B_POS[label].append(tuple(s))
    MIN_Z[label] = min(s[-1], e[-1])


def sim():
    number_that_fell = 0
    label_order = sorted(set(B.values()), key=MIN_Z.get)
    for label in label_order:
        z_offset = 9999
        for pos in B_POS[label]:
            if pos[-1] != MIN_Z[label]:
                continue
            z_offset_i = 0
            for z in range(pos[-1] - 1, 0, -1):
                check_pos = (pos[0], pos[1], z)
                if check_pos not in B:
                    z_offset_i += 1
                else:
                    break
            if z_offset_i < z_offset:
                z_offset = z_offset_i
        if z_offset > 0:
            # print(label)
            number_that_fell += 1
        # print(label, z_offset)
        for pos in B_POS[label]:
            # print(label, pos, (pos[0], pos[1], pos[2] - z_offset))
            del B[pos]
            B[(pos[0], pos[1], pos[2] - z_offset)] = label

    REST = {label: set() for label in B.values()}
    SUPPORT = {label: set() for label in B.values()}

    for brick, label in B.items():
        check_pos = (brick[0], brick[1], brick[2] - 1)
        if check_pos in B and B[check_pos] != label:
            REST[label].add(B[check_pos])
            SUPPORT[B[check_pos]].add(label)

    CANT_DIS = set()
    for label, s in REST.items():
        if len(s) == 1:
            CANT_DIS.add(next(iter(s)))
    return CANT_DIS, number_that_fell


# print(B)
# print(REST)
# print(REST[149])
# print(set(B.values()) - CANT_DIS)

cant_disintigrate, _ = sim()
ans = len(set(B.values()) - cant_disintigrate)
print(ans)

# B_POS = defaultdict(list)
# MIN_Z = defaultdict(lambda: 9999)
# for key, val in B.items():
#     B_POS[val].append(key)
#     MIN_Z[val] = min(MIN_Z[val], key[2])
# print(sim()[1])

acc = 0
for brick in cant_disintigrate:
    B_COPY = deepcopy(B)
    B_POS = defaultdict(list)
    MIN_Z = defaultdict(lambda: 9999)
    for key, val in B_COPY.items():
        if val == brick:
            del B[key]

    for key, val in B.items():
        B_POS[val].append(key)
        MIN_Z[val] = min(MIN_Z[val], key[2])

    # print()
    acc += sim()[1]
    B = B_COPY

print(acc)
# submit(acc)

from aoc.util import *

D = [a.splitlines() for a in get_data().split("\n\n")]


def is_ref(data: list[str], r):
    for i in range(r):
        if r + i >= len(data):
            return True
        if data[r - i - 1] != data[r + i]:
            return False
    return True


cols = 0
rows = 0
for pattern in D:
    orig_ref_line = [-1, -1]
    for c in range(1, len(pattern[0])):
        if is_ref(list(zip(*pattern)), c):
            # cols += c
            print("col", c)
            orig_ref_line[0] = c
            break

    for r in range(1, len(pattern)):
        if is_ref(pattern, r):
            print("row", r)
            # rows += r
            orig_ref_line[1] = r
            break

    found_new_line = False
    for r1, line in enumerate(pattern):
        for c1, char in enumerate(line):
            new_pattern = [list(line) for line in pattern]
            if char == "#":
                new_pattern[r1][c1] = "."
            else:
                new_pattern[r1][c1] = "#"
            for c in range(1, len(new_pattern[0])):
                if is_ref(list(zip(*new_pattern)), c) and c != orig_ref_line[0]:
                    cols += c
                    print("new col", c, "mod", (r1, c1))
                    found_new_line = True

            for r in range(1, len(new_pattern)):
                if is_ref(new_pattern, r) and r != orig_ref_line[1]:
                    print("new row", r, "mod", (r1, c1))
                    rows += r
                    found_new_line = True

            if found_new_line:
                break
        if found_new_line:
            break

submit(100 * rows + cols)

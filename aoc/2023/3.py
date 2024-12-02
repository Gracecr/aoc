from aoc.util import *

D = get_data().splitlines()
V = get_vectors(2, diag=True)
B = get_bounds(D)
vis = set()
nums = []
for row, line in enumerate(D):
    for col, c in enumerate(line):
        if c == "*":
            gr = []
            for n in get_neighbors((row, col), V, B):
                if D[n[0]][n[1]].isdigit():
                    pos = n[1]
                    while pos > 0 and D[n[0]][pos].isdigit():
                        pos -= 1
                    end_pos = n[1]
                    while end_pos < len(D[n[0]]) and D[n[0]][end_pos].isdigit():
                        end_pos += 1
                    if not D[n[0]][pos].isdigit():
                        num = D[n[0]][pos + 1 : end_pos]
                    else:
                        num = D[n[0]][pos:end_pos]
                    if (n[0], end_pos) not in vis:
                        gr.append(int(num))
                        vis.add((n[0], end_pos))
            if len(gr) == 2:
                nums.append(gr[0] * gr[1])

submit(sum(nums))

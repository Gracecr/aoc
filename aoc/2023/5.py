from aoc.util import *

D = get_data().splitlines()

maps = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
seeds = []
i = 0
for line in D:
    if "seeds:" in line:
        ranges = [int(w) for w in line[len("seeds: ") :].split()]
        seeds = list(zip(ranges[::2], ranges[1::2]))
    elif "-" in line:
        i += 1
    elif not line:
        continue
    else:
        dest_start, src_start, length = [int(w) for w in line.split()]
        maps[i].append((dest_start, src_start, length))

min_loc = 9999999999999999999999
for seed_range in seeds:
    for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
        loc = seed
        for map in maps:
            for r in map:
                if r[1] <= loc <= r[1] + r[2]:
                    loc = r[0] + (loc - r[1])
                    break
        if loc < min_loc:
            min_loc = loc
    print(f"Finished {seed_range}")

print(min_loc)
# submit(min_loc)

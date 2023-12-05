from aoc.util import *

D = get_data().splitlines()
# D = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4""".splitlines()

maps = [[], [],[],[], [], [], [], [], [], [], [], [], [], [], [], []]
seeds = []
i = 0
for line in D:
    if "seeds:" in line:
        ranges = [int(w) for w in line[len("seeds: "):].split()]
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

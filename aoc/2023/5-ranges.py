from aoc.util import *

D = get_data().splitlines()
D = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".splitlines()

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


def map_range(src_range: tuple[int, int], dest_range: tuple[int,int,int]) -> list[tuple[int, int]]:
    in_start, in_end = src_range
    dest_start, src_start, dest_len = dest_range
    dest_end = dest_start + dest_len
    src_end = src_start + dest_len

    if src_start <= in_start and src_end > in_start:
        #   |-----|
        # |---|
        # |---------|
        dstart = dest_start + (in_start - src_start)
        if in_end > src_end:
            #   |-----|
            # |---|
            dstart = dest_start + (in_start - src_start)
            return [
                (dstart, dstart + (src_end - in_start)),
                (src_end, src_end + (in_end - src_end))
            ]
        else:
            #   |-----|
            # |---------|
            return [
                (dstart, dstart + (in_end - in_start)),
            ]
    elif src_start > in_start and src_start < in_end:
        #   |-----|
        #    |---|
        #      |-----|
        if src_end < in_end:
            #   |-----|
            #    |---|
            return [
                (in_start, src_start),
                (dest_start, dest_end),
                (src_end, in_end)
            ]
        else:
            #   |-----|
            #      |-----|
            return [
                (dest_start, in_end),
            ]
    else:
        return [src_range]


locs = []
for seed_range in seeds:
    possible_locs = [seed_range[0], seed_range[0] + seed_range[1]]
    for map in maps[1:]:
        for r in map:
            new_possible_locs = map_range(possible_locs[0], r)
            for possible_loc in possible_locs:
                new_possible_locs.extend(map_range(possible_loc, r))
            possible_locs = new_possible_locs
    print(possible_locs)

min_loc = 99999999999999999999999
for loc in possible_locs:
    if loc[0] < min_loc:
        min_loc = loc
    
print(min_loc)
# print(min(locs))

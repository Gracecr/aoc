from aoc.util import *

D = get_data().splitlines()
# D = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1""".splitlines()


@functools.lru_cache
def backtrack(s: str, groups: tuple[int], prev: str = ""):
    if not groups:
        if "#" in s:
            return 0
        return 1

    if len(s) < groups[0] or s[0] == prev == "#":
        return 0

    if s[0] == ".":
        return backtrack(s[1:], groups, s[0])

    if s[0] == "?":
        return backtrack(s[1:], groups, ".") + backtrack("#" + s[1:], groups, prev)

    if any(char == "." for char in s[:groups[0]]):
        return 0

    return backtrack(s[groups[0]:], groups[1:], "#")

acc = 0
acc2 = 0
for line in D:
    springs, groups = line.split()
    groups = [int(i) for i in groups.split(",")]
    p2_springs = "?".join([springs for _ in range(5)])
    p2_groups = groups * 5
    p1_result = backtrack(springs, tuple(groups))
    p2_result = backtrack(p2_springs, tuple(p2_groups))
    acc += p1_result
    acc2 += p2_result

print(acc)
print(acc2)
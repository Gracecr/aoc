from aoc.util import *

D = get_data().splitlines()
# D = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1""".splitlines()


@functools.lru_cache
def backtrack(s: str, pat: tuple[int], last: str = ""):
    if not pat:
        if "#" in s:
            return 0
        return 1
    
    if len(s) < pat[0] or s[0] == last == "#":
        return 0

    if s[0] == ".":
        return backtrack(s[1:], pat, s[0])

    if s[0] == "?":
        return backtrack(s[1:], pat, ".") + backtrack("#" + s[1:], pat, last)

    if any(True for char in s[:pat[0]] if char == "."):
        return 0
        
    return backtrack(s[pat[0]:], pat[1:], "#")

acc = 0
acc2 = 0
for line in D:
    springs, pattern = line.split()
    pattern = [int(i) for i in pattern.split(",")]
    p2_springs = "?".join([springs for _ in range(5)])
    p2_pattern = pattern * 5
    p1_result = backtrack(springs, tuple(pattern))
    p2_result = backtrack(p2_springs, tuple(p2_pattern))
    acc += p1_result
    acc2 += p2_result

print(acc)
print(acc2)
from aoc.util import *

d = [d for d in get_data().splitlines()]

b = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]

nums = []
for s in d:
    n = ""
    num2 = []
    pos_d = {}
    for p in b:
        if p[0] in s:
            pos_d[s.index(p[0])] = p[1]
            pos_d[s.rindex(p[0])] = p[1]
    for i, c in enumerate(s):
        if c in "123456789":
            pos_d[i] = c
    nums.append(int(pos_d[min(pos_d.keys())] + pos_d[max(pos_d.keys())]))

print(nums)
for t, y in zip(nums, d):
    print(t, y)
print(sum(nums))
submit(sum(nums))
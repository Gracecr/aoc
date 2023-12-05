from aoc.util import *

d = [int(d) for d in get_data().splitlines()]

for nums in itertools.combinations(d, 3):
    if sum(nums) == 2020:
        print(functools.reduce(operator.mul, nums))

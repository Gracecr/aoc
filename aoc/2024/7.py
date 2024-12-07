import itertools
import operator
from typing import Callable

from aoc import util as u

D = u.get_data().splitlines()
P1_OPS = [operator.mul, operator.add]
P2_OPS = [operator.mul, operator.add, lambda x, y: int(str(x) + str(y))]


def test(ans: int, values: list[int], ops: list[Callable[[int, int], int]]) -> int:
    for ops_list in itertools.product(*([ops] * (len(values) - 1))):
        s = values[0]
        for op, value in zip(ops_list, values[1:]):
            s = op(s, value)
        if s == ans:
            return ans
        elif s > ans:
            # Thanks to @toothlessG22 for the optimization
            return 0
    return 0


p1 = 0
p2 = 0
for line in D:
    ans, values = line.split(": ")
    ans = int(ans)
    values = list(map(int, values.split()))
    p1 += test(ans, values, P1_OPS)
    p2 += test(ans, values, P2_OPS)

print(p1)
print(p2)

import functools
from collections import defaultdict

from sympy import solve, symbols
from sympy.utilities.misc import as_int

from aoc import util as u

D = u.get_data().split("\n\n")
P2 = 10000000000000


@functools.cache
def get_num_tokens_to_reach_target(
    a: tuple[int, int], b: tuple[int, int], x: int, y: int
):
    if x == 0 and y == 0:
        return 0

    test = [10**9]
    if x >= a[0] and y >= a[1]:
        test.append(3 + get_num_tokens_to_reach_target(a, b, x - a[0], y - a[1]))
    if x >= b[0] and y >= b[1]:
        test.append(1 + get_num_tokens_to_reach_target(a, b, x - b[0], y - b[1]))

    return min(test)


p1 = 0
p2 = 0
for i, machine_def in enumerate(D):
    buttons = defaultdict(list)
    PRIZE = (0, 0)

    for line in machine_def.splitlines():
        l = line.split(": ")
        if line.startswith("Button"):
            button = l[0][-1]
            for v in l[1].split(", "):
                buttons[button].append(int(v[2:]))
        elif line.startswith("Prize:"):
            l2 = l[1].split(", ")
            PRIZE = int(l2[0][2:]), int(l2[1][2:])

    a_count, b_count = symbols("a_count b_count")
    solution = solve(
        [
            a_count * buttons["A"][0] + b_count * buttons["B"][0] - PRIZE[0] - P2,
            a_count * buttons["A"][1] + b_count * buttons["B"][1] - PRIZE[1] - P2,
        ],
        [a_count, b_count],
        dict=True,
    )
    assert len(solution) > 0
    solution = solution[0]
    try:
        p2 += 3 * as_int(solution[a_count]) + as_int(solution[b_count])
    except ValueError:
        pass

    num_tokens = get_num_tokens_to_reach_target(
        tuple(buttons["A"]), tuple(buttons["B"]), PRIZE[0], PRIZE[1]
    )
    if num_tokens != 10**9:
        p1 += num_tokens


print(p1)
print(p2)

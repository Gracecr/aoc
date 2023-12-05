import sys

sys.path.append("C:/Users/cgrac/dev/aoc")
from util import get_data, submit  # pylint: disable=unused-import

import operator

OPS = {
    "+": operator.add,
    "*": operator.mul,
}


def eval_eq(eq: list):
    val = 0
    op = operator.add
    while eq:
        c = eq.pop(0)
        if isinstance(c, int):
            val = op(val, c)
        elif isinstance(c, list):
            val = op(val, eval_eq(c))
        elif c in OPS:
            op = OPS[c]
        else:
            print("wtf?")

    return val


def eval_eq2(eq: list):
    val = 0
    op = operator.add
    multiply_num = 1
    while eq:
        c = eq.pop(0)
        if isinstance(c, int):
            val = op(val, c * multiply_num)
        elif isinstance(c, list):
            val = op(val, eval_eq2(c) * multiply_num)
        elif c == "*":
            multiply_num = val
            val = 0
        elif c == "+":
            continue
        else:
            print("wtf?")

    return val


def part_one(data: str):
    running_sum = 0
    for line in data.splitlines():
        eq_str = (
            "["
            + line.replace("(", "[")
            .replace(")", "]")
            .replace(" ", ",")
            .replace("+", "'+'")
            .replace("*", "'*'")
            + "]"
        )
        eq = eval(eq_str)
        running_sum += eval_eq(eq)
    return running_sum


def part_two(data: str):
    running_sum = 0
    for line in data.splitlines():
        eq_str = (
            "["
            + line.replace("(", "[")
            .replace(")", "]")
            .replace(" ", ",")
            .replace("+", "'+'")
            .replace("*", "'*'")
            + "]"
        )
        eq = eval(eq_str)
        running_sum += eval_eq2(eq)
    return running_sum


if __name__ == "__main__":
    data_ = get_data()
    PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    # submit(PART_ONE_ANSWER)
    submit(PART_TWO_ANSWER)

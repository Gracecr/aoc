from functools import lru_cache
import sys

sys.path.append("C:/Users/cgrac/dev/aoc")
from util import get_data, submit  # pylint: disable=unused-import


def part_one(data: str):
    adapters = []
    for line in data.splitlines():
        adapters.append(int(line))

    adapters.append(0)
    adapters.sort()
    diffs = [a - b for a, b in zip(adapters, adapters[1:] + [max(adapters) + 3])]
    num_1 = 0
    num_2 = 0
    for n in diffs:
        if n == -1:
            num_1 += 1
        elif n == -3:
            num_2 += 1
    return num_1 * num_2


@lru_cache(maxsize=3)
def possibilities(item, adapters):
    x = [z for z in range(item - 3, item) if z in adapters]
    if item == 0:
        return 1
    return sum(possibilities(i, adapters) for i in x)


def part_two(data: str):
    adapters = []
    for line in data.splitlines():
        adapters.append(int(line))

    adapters.append(0)
    adapters.sort()
    return possibilities(max(adapters) + 3, tuple(adapters))


if __name__ == "__main__":
    data_ = get_data()
    PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    # submit(PART_ONE_ANSWER)
    submit(PART_TWO_ANSWER)

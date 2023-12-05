import sys
import copy
from collections import defaultdict

sys.path.append("C:/Users/cgrac/dev/aoc")
from util import get_data, submit  # pylint: disable=unused-import


def print_d(d):
    s = [list("..................") for _ in range(12)]
    for r, c in d:
        if d[(r, c)]:
            s[r][c] = d[(r, c)]
    for ss in s:
        print("".join(ss))
    print()


def tick(d: dict[tuple[int, int], str]):
    new_d = copy.deepcopy(d)
    seats = list(d.keys())
    for r, c in seats:
        if d[(r, c)] == "#":
            num_adj_occupied = 0
            if d[(r + 1, c)] == "#":
                num_adj_occupied += 1
            if d[(r - 1, c)] == "#":
                num_adj_occupied += 1
            if d[(r, c + 1)] == "#":
                num_adj_occupied += 1
            if d[(r, c - 1)] == "#":
                num_adj_occupied += 1
            if d[(r + 1, c + 1)] == "#":
                num_adj_occupied += 1
            if d[(r + 1, c - 1)] == "#":
                num_adj_occupied += 1
            if d[(r - 1, c - 1)] == "#":
                num_adj_occupied += 1
            if d[(r - 1, c + 1)] == "#":
                num_adj_occupied += 1

            if num_adj_occupied >= 4:
                new_d[(r, c)] = "L"

        if d[(r, c)] == "L":
            if (
                d[(r + 1, c)] != "#"
                and d[(r - 1, c)] != "#"
                and d[(r, c + 1)] != "#"
                and d[(r, c - 1)] != "#"
                and d[(r + 1, c + 1)] != "#"
                and d[(r + 1, c - 1)] != "#"
                and d[(r - 1, c - 1)] != "#"
                and d[(r - 1, c + 1)] != "#"
            ):
                new_d[(r, c)] = "#"
    return new_d


def part_one(data: str):
    d = defaultdict(list)
    for r, line in enumerate(data.splitlines()):
        for c, seat in enumerate(line):
            if seat == "L":
                d[(r, c)] = seat

    num_ticks = 0
    cur_d = d
    while True:
        num_ticks += 1
        # print_d(cur_d)
        new_d = tick(cur_d)
        num_diffs = 0
        for r, c in cur_d:
            if cur_d[(r, c)] and new_d[(r, c)] != cur_d[(r, c)]:
                num_diffs += 1
        if num_diffs == 0:
            num_occupied = 0
            for r, c in cur_d:
                if cur_d[(r, c)] == "#":
                    num_occupied += 1
            return num_occupied

        cur_d = new_d


def part_two(data: str):
    return "TODO"


if __name__ == "__main__":
    data_ = get_data()
    PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    submit(PART_ONE_ANSWER)
    # submit(PART_TWO_ANSWER)

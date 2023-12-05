import math
import sys

sys.path.append("C:/Users/cgrac/dev/aoc")
from util import get_data, submit  # pylint: disable=unused-import


NUM_ROWS = 128
NUM_COLS = 8


def calc_id(row, col):
    return row * 8 + col


def part_one(data: str):
    seats = []
    for line in data.splitlines():
        row_max = NUM_ROWS
        row_min = 0
        col_max = NUM_COLS
        col_min = 0
        for l in line:
            if l == "F":
                row_max = math.floor((row_max + row_min) / 2)
            elif l == "B":
                row_min = math.ceil((row_max + row_min) / 2)
            elif l == "L":
                col_max = math.floor((col_max + col_min) / 2)
            elif l == "R":
                col_min = math.ceil((col_max + col_min) / 2)
        row = row_max - 1
        col = col_max - 1
        seats.append((row, col))
    return max(calc_id(*seat) for seat in seats)


def part_two(data: str):
    seats = []
    for line in data.splitlines():
        row_max = NUM_ROWS
        row_min = 0
        col_max = NUM_COLS
        col_min = 0
        for l in line:
            if l == "F":
                row_max = math.floor((row_max + row_min) / 2)
            elif l == "B":
                row_min = math.ceil((row_max + row_min) / 2)
            elif l == "L":
                col_max = math.floor((col_max + col_min) / 2)
            elif l == "R":
                col_min = math.ceil((col_max + col_min) / 2)
        row = row_max - 1
        col = col_max - 1
        seats.append((row, col))

    seat_ids = set()
    for seat in seats:
        seat_ids.add(calc_id(*seat))

    for i in range(37, 943):
        if i in seat_ids:
            continue
        if i + 1 in seat_ids and i - 1 in seat_ids:
            print(i)


if __name__ == "__main__":
    data_ = get_data()
    PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    # submit(PART_ONE_ANSWER)
    # submit(PART_TWO_ANSWER)

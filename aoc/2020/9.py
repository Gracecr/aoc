import sys

sys.path.append("C:/Users/cgrac/dev/aoc")
from util import get_data, submit  # pylint: disable=unused-import


PREAMBLE_LENGTH = 25


def is_sum_of_2(num, back_check):
    for pre1 in back_check:
        for pre2 in back_check:
            if pre1 + pre2 == num:
                return True
    return False


def part_one(data: str):
    nums = []
    for line in data.splitlines():
        nums.append(int(line))
    for i, num in enumerate(nums):
        if i < PREAMBLE_LENGTH:
            continue
        if not is_sum_of_2(num, nums[i - PREAMBLE_LENGTH : i]):
            return num


def part_two(data: str):
    invalid_num = part_one(data)
    nums = []
    for line in data.splitlines():
        nums.append(int(line))

    start_cur = 0
    end_cur = 0
    while True:
        cur_sum = sum(nums[start_cur:end_cur])
        if cur_sum > invalid_num:
            start_cur += 1
        elif cur_sum < invalid_num:
            end_cur += 1
        else:
            return min(nums[start_cur:end_cur]) + max(nums[start_cur:end_cur])


if __name__ == "__main__":
    data_ = get_data()
    PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    # submit(PART_ONE_ANSWER)
    submit(PART_TWO_ANSWER)

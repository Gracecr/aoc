import sys

sys.path.append("C:/Users/cgrac/dev/aoc")
from util import get_data, submit  # pylint: disable=unused-import


def part_one(data: str):
    s = 0
    for group in data.split("\n\n"):
        g = group.replace("\n", "")
        s += len(set(g))
    return s


def part_two(data: str):
    s = 0
    for group in data.split("\n\n"):
        person_answers: list[set] = []
        for person in group.splitlines():
            person_answers.append(set(person))
        s += len(person_answers[0].intersection(*person_answers))

    return s


if __name__ == "__main__":
    data_ = get_data()

    PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    # submit(PART_ONE_ANSWER)
    submit(PART_TWO_ANSWER)

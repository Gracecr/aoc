import sys

sys.path.append("C:/Users/cgrac/dev/aoc")
from util import get_data, submit  # pylint: disable=unused-import


def part_one(data: str):
    instructions = []
    for line in data.splitlines():
        op, val = line.split()
        instructions.append((op, int(val)))

    return check_for_loop(instructions)[1]


def check_for_loop(instructions):
    acc = 0
    current_instruction = 0
    visited = set()
    while (
        current_instruction < len(instructions) and current_instruction not in visited
    ):
        instruction = instructions[current_instruction]
        visited.add(current_instruction)
        if instruction[0] == "nop":
            current_instruction += 1
        elif instruction[0] == "acc":
            acc += instruction[1]
            current_instruction += 1
        elif instruction[0] == "jmp":
            current_instruction += instruction[1]
    return current_instruction == len(instructions), acc


def part_two(data: str):
    instructions = []
    for line in data.splitlines():
        op, val = line.split()
        instructions.append([op, int(val)])

    for instruction in instructions:
        if instruction[0] == "nop":
            instruction[0] = "jmp"
            if check_for_loop(instructions)[0]:
                return check_for_loop(instructions)[1]
            instruction[0] = "nop"
        if instruction[0] == "jmp":
            instruction[0] = "nop"
            if check_for_loop(instructions)[0]:
                return check_for_loop(instructions)[1]
            instruction[0] = "jmp"


if __name__ == "__main__":
    data_ = get_data()
    PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    # submit(PART_ONE_ANSWER)
    # submit(PART_TWO_ANSWER)

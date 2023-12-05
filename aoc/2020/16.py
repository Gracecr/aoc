import sys

sys.path.append("C:/Users/cgrac/dev/aoc")
from util import get_data, submit  # pylint: disable=unused-import


def apply_mask(mask: str, num: int):
    num_bit_repr = list(bin(num)[2:].zfill(len(mask)))
    for i, mask_bit in enumerate(mask):
        if mask_bit != "X":
            num_bit_repr[i] = mask_bit

    return int("".join(num_bit_repr), 2)


def part_one(data: str):
    memory = {}
    mask = None
    for line in data.splitlines():
        if "mask" in line:
            mask = line[len("mask = ") :]
        else:
            addr = int(line[line.index("[") + 1 : line.index("]")])
            val = int(line[line.index("=") + 1 :])
            memory[addr] = apply_mask(mask, val)

    return sum(memory.values())


def apply_mask2(mask: str, num: int):
    num_bit_repr = list(bin(num)[2:].zfill(len(mask)))
    mask_list = list(mask)
    for i, mask_bit in enumerate(mask):
        if mask_bit == "1":
            num_bit_repr[i] = mask_bit
        if mask_bit == "X":
            mask_list[i] = "0"
            num_bit_repr[i] = "0"
            yield from apply_mask2("".join(mask_list), int("".join(num_bit_repr), 2))
            num_bit_repr[i] = "1"
            yield from apply_mask2("".join(mask_list), int("".join(num_bit_repr), 2))

    yield int("".join(num_bit_repr), 2)


def part_two(data: str):
    memory = {}
    mask = None
    for line in data.splitlines():
        if "mask" in line:
            mask = line[len("mask = ") :]
        else:
            addr = int(line[line.index("[") + 1 : line.index("]")])
            val = int(line[line.index("=") + 1 :])
            for addr in apply_mask2(mask, addr):
                memory[addr] = val

    return sum(memory.values())


if __name__ == "__main__":
    data_ = get_data()
    PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    # submit(PART_ONE_ANSWER)
    # submit(PART_TWO_ANSWER)

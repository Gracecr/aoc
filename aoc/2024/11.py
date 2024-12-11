import functools

from aoc import util as u

D = u.get_data()
STONES = [int(s) for s in D.split()]


@functools.cache
def process_stone(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1

    if stone == 0:
        return process_stone(1, blinks - 1)

    if len(str(stone)) % 2 == 0:
        left = int(str(stone)[: len(str(stone)) // 2])
        right = int(str(stone)[len(str(stone)) // 2 :])
        return process_stone(left, blinks - 1) + process_stone(right, blinks - 1)

    return process_stone(2024 * stone, blinks - 1)


print(sum(process_stone(stone, 25) for stone in STONES))
print(sum(process_stone(stone, 75) for stone in STONES))

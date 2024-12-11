import functools

from aoc import util as u

D = u.get_data()
STONES = [int(s) for s in D.split()]


@functools.lru_cache(maxsize=100000)
def proccess_stone(stone: int, blinks: int) -> tuple[int]:
    if blinks == 0:
        return 1

    if stone == 0:
        return proccess_stone(1, blinks - 1)

    if len(str(stone)) % 2 == 0:
        left = int(str(stone)[: len(str(stone)) // 2])
        right = int(str(stone)[len(str(stone)) // 2 :])
        return proccess_stone(left, blinks - 1) + proccess_stone(right, blinks - 1)

    return proccess_stone(2024 * stone, blinks - 1)


print(sum(proccess_stone(stone, 25) for stone in STONES))
print(sum(proccess_stone(stone, 75) for stone in STONES))

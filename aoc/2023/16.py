from enum import Enum

from aoc.util import *

D = get_data().splitlines()
# D = r""".|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|....""".splitlines()


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


mirror_dir_map: dict[str, dict[Direction, Direction]] = {
    "/": {
        Direction.UP: Direction.RIGHT,
        Direction.DOWN: Direction.LEFT,
        Direction.LEFT: Direction.DOWN,
        Direction.RIGHT: Direction.UP,
    },
    "\\": {
        Direction.UP: Direction.LEFT,
        Direction.DOWN: Direction.RIGHT,
        Direction.LEFT: Direction.UP,
        Direction.RIGHT: Direction.DOWN,
    },
}


@dataclasses.dataclass(frozen=True)
class Beam:
    direction: Direction
    position: tuple[int, int]


def calc_energized(start_beam: Beam) -> int:
    V: set[Beam] = set()

    def f(b: Beam):
        if b in V:
            return

        if 0 <= b.position[0] < len(D) and 0 <= b.position[1] < len(D[0]):
            V.add(b)
        else:
            return

        ch = D[b.position[0]][b.position[1]]
        if (
            ch == "."
            or (ch == "|" and b.direction in (Direction.UP, Direction.DOWN))
            or (ch == "-" and b.direction in (Direction.RIGHT, Direction.LEFT))
        ):
            f(Beam(b.direction, addt(b.position, b.direction.value)))

        elif ch in "/\\":
            new_direction = mirror_dir_map[ch][b.direction]
            f(Beam(new_direction, addt(b.position, new_direction.value)))

        elif ch == "|":
            for direction in (Direction.UP, Direction.DOWN):
                f(Beam(direction, addt(b.position, direction.value)))

        elif ch == "-":
            for direction in (Direction.RIGHT, Direction.LEFT):
                f(Beam(direction, addt(b.position, direction.value)))

    f(start_beam)
    return len({b.position for b in V})


print(calc_energized(Beam(Direction.RIGHT, (0, 0))))


energized_counts = []
for r in range(len(D)):
    energized_counts.append(calc_energized(Beam(Direction.RIGHT, (r, 0))))
    energized_counts.append(calc_energized(Beam(Direction.LEFT, (r, len(D[0]) - 1))))

for c in range(len(D[0])):
    energized_counts.append(calc_energized(Beam(Direction.DOWN, (0, c))))
    energized_counts.append(calc_energized(Beam(Direction.UP, (len(D) - 1, c))))

print(max(energized_counts))

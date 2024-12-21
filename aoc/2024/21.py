from functools import cache

from aoc import util as u

D = u.get_data().splitlines()
G_NUMERIC = u.nx.Graph()
for x in range(3):
    for y in range(4):
        if y == 3 and x == 0:
            continue
        for n in u.get_neighbors((x, y), u.get_vectors(2), ((0, 3), (0, 4))):
            if n != (0, 3):
                G_NUMERIC.add_edge((x, y), n)
G_DIRECTIONAL = u.nx.Graph()
G_DIRECTIONAL.add_edge((1, 0), (2, 0))
G_DIRECTIONAL.add_edge((2, 0), (2, 1))
G_DIRECTIONAL.add_edge((2, 1), (1, 1))
G_DIRECTIONAL.add_edge((1, 0), (1, 1))
G_DIRECTIONAL.add_edge((0, 1), (1, 1))


DIRS = {
    (1, 0): "v",
    (-1, 0): "^",
    (0, 1): ">",
    (0, -1): "<",
}


def convert_path_to_moves(path) -> str:
    return (
        "".join(DIRS[(n2[1] - n1[1], n2[0] - n1[0])] for n1, n2 in zip(path, path[1::]))
        + "A"
    )


class Keypad:
    def __init__(self, x: int, y: int, map_: tuple[tuple], g):
        self.x = x
        self.y = y
        self._map = map_
        self._bad_y, self._bad_x = next(
            (r_i, row.index(None)) for r_i, row in enumerate(self._map) if None in row
        )
        self.g = g

    @property
    def ch(self) -> str:
        return self._map[self.y][self.x]

    def move(self, ch: str) -> str:
        ch_pos = next(
            (r_i, row.index(ch)) for r_i, row in enumerate(self._map) if ch in row
        )
        return self._move(ch_pos[1], ch_pos[0])

    def _move(self, x: int, y: int) -> str:
        # dx = x - self.x
        # dy = y - self.y
        # horiz = ">" * dx if dx > 0 else "<" * abs(dx)
        # vert = "v" * dy if dy > 0 else "^" * abs(dy)
        # ret = horiz + vert
        # if self.y == self._bad_y:
        #     ret = vert + horiz
        # self.x = x
        # self.y = y
        # assert self._map[self.y][self.x] is not None
        # return ret
        paths = list(u.nx.all_shortest_paths(self.g, (self.x, self.y), (x, y)))
        paths = [convert_path_to_moves(path) for path in paths]
        self.x = x
        self.y = y
        return paths if paths else "A"


class DirectionalKeypad(Keypad):
    def __init__(self):
        super().__init__(
            2,
            0,
            (
                (None, "^", "A"),
                ("<", "v", ">"),
            ),
            G_DIRECTIONAL,
        )


class NumericKeypad(Keypad):
    def __init__(self):
        super().__init__(
            2,
            3,
            (
                ("7", "8", "9"),
                ("4", "5", "6"),
                ("1", "2", "3"),
                (None, "0", "A"),
            ),
            G_NUMERIC,
        )


@cache
def move_multi_keypad(moves: str, depth: int = 25):
    keypad = NumericKeypad() if depth == 25 else DirectionalKeypad()
    ret = 0
    for ch in moves:
        possible_moves = keypad.move(ch)
        if depth == 0:
            ret += len(possible_moves[0])
            continue
        ret += min(
            move_multi_keypad(possible_move, depth - 1)
            for possible_move in possible_moves
        )
    return ret


# def move_multi_keypad(moves: str, 0) -> str:
#     for keypad in keypads:
#         ret = ""
#         for move in moves:
#             ret += keypad.move(move) + "A"
#         moves = ret
#         # print(ret)
#     return ret


def solve(code: str) -> int:
    numeric = int(code[:-1])
    move_length = move_multi_keypad(code)
    print(numeric, move_length)
    return numeric * move_length


p1 = 0
for line in D:
    p1 += solve(line)

print(p1)

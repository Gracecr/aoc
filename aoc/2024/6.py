from aoc import util as u

type Point = tuple[int, int]

right_turn = {
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
}

D = [[l for l in line] for line in u.get_data().splitlines()]
for r in range(len(D)):
    for c in range(len(D[r])):
        if D[r][c] == "^":
            guard = (r, c)
            break

B = u.get_bounds(D)

direction = (-1, 0)
p1 = 0
p2 = 0


def is_cycle(obstacle_pos: Point, guard_pos: Point, guard_dir: Point) -> bool:
    visited = set()
    while (guard_pos, guard_dir) not in visited:
        visited.add((guard_pos, guard_dir))
        new_guard_pos = u.addt(guard_pos, guard_dir)
        if not u.is_in_bounds(B, new_guard_pos):
            return False

        if (
            D[new_guard_pos[0]][new_guard_pos[1]] == "#"
            or new_guard_pos == obstacle_pos
        ):
            guard_dir = right_turn[guard_dir]
        else:
            guard_pos = new_guard_pos

    return True


for r in range(len(D)):
    for c in range(len(D[r])):
        if is_cycle((r, c), guard, direction):
            p2 += 1
    print(r / len(D))

print(p2)

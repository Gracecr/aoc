from collections import deque

from aoc import util as u

D = u.get_data().splitlines()
V = u.get_vectors(2)
B = u.get_bounds(D)

VISITED = set()


def bfs(pos: tuple[int, int]) -> int:
    area = 0
    perimeter = 0
    q = deque([pos])
    shape = set()
    perimeter_shape = set()

    while q:
        n = q.popleft()
        n_v = D[n[0]][n[1]]
        shape.add(n)
        area += 1

        for v in V:
            v = int(v[0]), int(v[1])
            neigh = (int(n[0]) + int(v[0]), int(n[1]) + int(v[1]))
            if not u.is_in_bounds(B, neigh):
                perimeter += 1
                perimeter_shape.add((neigh, v))
                continue
            if D[neigh[0]][neigh[1]] == n_v:
                if neigh in VISITED:
                    continue
                VISITED.add(neigh)
                q.append(neigh)
            else:
                perimeter += 1
                perimeter_shape.add((neigh, v))
    return area, perimeter, perimeter_shape, shape


def count_sides(
    perimeter_shape: set[tuple[int, int]], shape: set[tuple[int, int]]
) -> int:
    perimeter_shape = {
        ((int(a[0][0]), int(a[0][1])), (int(a[1][0]), int(a[1][1])))
        for a in list(perimeter_shape)
    }
    shape = {(int(a[0]), int(a[1])) for a in list(shape)}
    check_dirs = [(-1, 0), (0, -1)]

    reduced_perimeter_shape = set(perimeter_shape)
    for pos, direction in list(perimeter_shape):
        if any((u.addt(pos, v), direction) in perimeter_shape for v in check_dirs):
            reduced_perimeter_shape.remove((pos, direction))

    return len(reduced_perimeter_shape)


p1 = 0
p2 = 0
for r, line in enumerate(D):
    for c, ch in enumerate(line):
        if (r, c) not in VISITED:
            VISITED.add((r, c))
            area, perimeter, perimeter_shape, shape = bfs((r, c))
            # print(ch, area, perimeter)
            # p1 += area * perimeter
            sides = count_sides(perimeter_shape, shape)
            print(ch, area, sides)
            p2 += sides * area
print(p1)
print(p2)

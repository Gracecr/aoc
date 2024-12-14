from aoc import util as u

D = u.get_data().splitlines()

X = 101
Y = 103
SECONDS = 100

MACHINES = []
POS_AFTER_SECONDS = []

for line in D:
    px, py, vx, vy = map(int, u.re.findall(r"(-?\d+)", line))
    MACHINES.append(([px, py], (vx, vy)))
    POS_AFTER_SECONDS.append(((px + vx * SECONDS) % X, (py + vy * SECONDS) % Y))


def print_pos(positions: list[tuple[int]]):
    for x in range(X):
        for y in range(Y):
            if (x, y) in positions:
                print("#", end="")
            else:
                print(" ", end="")
        print()


# for s in range(10000):
#     print(s + 1)
#     for machine in MACHINES:
#         vx, vy = machine[1]
#         machine[0][0] = (machine[0][0] + vx) % X
#         machine[0][1] = (machine[0][1] + vy) % Y
#     print_pos(set(tuple(machine[0]) for machine in MACHINES))
#     print("=" * 100)


QUADRANTS = [[], [], [], []]

for x, y in POS_AFTER_SECONDS:
    quadrant = 0
    if 0 <= x < X // 2:
        if 0 <= y < Y // 2:
            quadrant = 1
        elif Y // 2 < y < Y:
            quadrant = 3
    elif X // 2 < x < X:
        if 0 <= y < Y // 2:
            quadrant = 2
        elif Y // 2 < y < Y:
            quadrant = 4
    if quadrant != 0:
        QUADRANTS[quadrant - 1].append((x, y))


p1 = len(QUADRANTS[0]) * len(QUADRANTS[1]) * len(QUADRANTS[2]) * len(QUADRANTS[3])
p2 = 7623  # Bruh

print(p1)
print(p2)

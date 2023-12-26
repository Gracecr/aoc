from aoc.util import *

D = get_data().splitlines()
# D = """19, 13, 30 @ -2,  1, -2
# 18, 19, 22 @ -1, -1, -2
# 20, 25, 34 @ -2, -2, -4
# 12, 31, 28 @ -1, -2, -1
# 20, 19, 15 @  1, -5, -3""".splitlines()
H = []

MIN = 200000000000000
MAX = 400000000000000
# MIN = 7
# MAX = 27

for line in D:
    pos, vel = line.split(" @ ")
    pos = [int(i) for i in pos.split(", ")]
    vel = [int(i) for i in vel.split(", ")]
    H.append((tuple(pos), tuple(vel)))


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return False

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


from sympy import Eq, solve, symbols

x, y, z, vx, vy, vz = symbols("x, y, z, vx, vy, vz")
t = []
eqs = []
for i, h in enumerate(H[:5]):
    t.append(symbols(f"t{i}"))
    eqs.append(Eq(x + vx * t[i], h[0][0] + h[1][0] * t[i]))
    eqs.append(Eq(y + vy * t[i], h[0][1] + h[1][1] * t[i]))
    eqs.append(Eq(z + vz * t[i], h[0][2] + h[1][2] * t[i]))

print(sum(solve(eqs, [x, y, z, vx, vy, vz, *t])[0][:3]))


# hailstones_that_intersect = []
# for h1, h2 in itertools.combinations(H, 2):
# intersection = line_intersection(
#     (h1[0], addt(h1[0][:-1], h1[1][:-1])), (h2[0], addt(h2[0][:-1], h2[1][:-1]))
# )

# # Don'd intersect
# if not intersection:
#     continue

# # Check that t is positive
# if not (((intersection[0] - h1[0][0]) < 0) == (h1[1][0] < 0)):
#     continue
# if not (((intersection[1] - h1[0][1]) < 0) == (h1[1][1] < 0)):
#     continue
# if not (((intersection[0] - h2[0][0]) < 0) == (h2[1][0] < 0)):
#     continue
# if not (((intersection[1] - h2[0][1]) < 0) == (h2[1][1] < 0)):
#     continue

# if intersection and MIN <= intersection[0] <= MAX and MIN <= intersection[1] <= MAX:
#     hailstones_that_intersect.append((h1, h2))

# print(hailstones_that_intersect)
# submit(len(hailstones_that_intersect))

from aoc.util import *

D = get_data().splitlines()
VEC = get_vectors(2)
R = len(D)
C = len(D[0])
NUM = 26501365

start = (0, 0)
for r, line in enumerate(D):
    if "S" in line:
        start = r, line.index("S")


NUM_STEPS = (NUM % R) + R * 3
Q = deque([(start, 0)])
V = set([(start, 0)])
num_reachable = defaultdict(int)
while Q:
    pos, steps = Q.popleft()

    num_reachable[steps] += 1

    for n in get_neighbors(pos, VEC):
        ch = D[n[0] % len(D)][n[1] % len(D[0])]
        a = (n, steps + 1)
        if a not in V and ch != "#" and steps < NUM_STEPS:
            V.add(a)
            Q.append(a)

x = [NUM % R + R * i for i in range(3)]
y = [num_reachable[i] for i in x]
print(x)
print(y)
n = NUM // R
print(np.polyfit(range(3), y, 2))
print(np.poly1d(np.polyfit(range(3), y, 2))(NUM // R))

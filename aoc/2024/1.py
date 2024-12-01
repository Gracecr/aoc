from collections import Counter

from aoc import util as u

D = u.get_data().splitlines()

L1 = []
L2 = []
for line in D:
    a = line.split()
    L1.append(int(a[0]))
    L2.append(int(a[1]))

L1.sort()
L2.sort()
ans2 = 0
ans = 0
c = Counter(L2)
for a, b in zip(L1, L2):
    ans += a * c[a]
    ans2 += abs(a - b)

print(ans2)
print(ans)
# u.submit(ans)

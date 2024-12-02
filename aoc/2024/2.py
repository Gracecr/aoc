from aoc import util as u

D = u.get_data().splitlines()


def check_safe(levels: list) -> bool:
    sign = 1 if levels[0] > levels[1] else -1
    return all(1 <= (l1 - l2) * sign <= 3 for l1, l2 in zip(levels, levels[1:]))


p1 = 0
p2 = 0
for line in D:
    levels = [int(w) for w in line.split()]
    if check_safe(levels):
        p1 += 1
        p2 += 1
    else:
        for i in range(len(levels)):
            if check_safe(levels[:i] + levels[i + 1 :]):
                p2 += 1
                break


print(p1)
print(p2)
# u.submit(p1)
# u.submit(p2)

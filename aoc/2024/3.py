from aoc import util as u

D = u.get_data()
regex = u.re.compile(r"mul\((\d+),(\d+)\)")
do_regex = u.re.compile(r"do\(\)")
dont_regex = u.re.compile(r"don't\(\)")


p1 = 0
p2 = 0

dos = [0] + [m.start() for m in do_regex.finditer(D)]
donts = [m.start() for m in dont_regex.finditer(D)]


def find_closest_value(lst, target):
    last_v = -1
    for v in lst:
        if v > target:
            return last_v
        last_v = v
    return last_v


for match in regex.finditer(D):
    closest_do = find_closest_value(dos, match.start())
    closest_dont = find_closest_value(donts, match.start())
    if closest_do > closest_dont:
        p2 += int(match[1]) * int(match[2])

    p1 += int(match[1]) * int(match[2])


print(p1)
print(p2)
# u.submit(p1)
# u.submit(p2)

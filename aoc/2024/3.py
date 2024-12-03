from aoc import util as u

D = u.get_data()
regex = u.re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")

p1 = 0
p2 = 0

mul_enabled = True
for match in regex.finditer(D):
    if match.group(0).startswith("mul"):
        value = int(match[1]) * int(match[2])
        p1 += value
        if mul_enabled:
            p2 += value
    else:
        mul_enabled = match.group(0) == "do()"

print(p1)
print(p2)
# u.submit(p1)
# u.submit(p2)

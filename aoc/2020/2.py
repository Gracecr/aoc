from aoc.util import *

regex = r"^(\d+)-(\d+) (\w+): (\w+)$"
num_valid = 0
for line in get_data().splitlines():
    r1, r2, letter, passwd = re.search(regex, line).groups()
    if (passwd[int(r1)-1] == letter) != (passwd[int(r2)-1] == letter):
        num_valid+=1
print(num_valid)
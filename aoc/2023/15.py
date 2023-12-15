from aoc.util import *

D = get_data()

def f(s: str):
    cur_val = 0
    for char in s:
        cur_val += ord(char)
        cur_val *= 17
        cur_val %= 256
    return cur_val

print(sum(f(l) for l in D.split(",")))


V = [{} for _ in range(256)]
for d in D.split(","):
    if "-" in d:
        label = d[:-1]
        box = f(label)
        if label in V[box]:
            del V[box][label]
        
    elif "=" in d:
        label, focal_length = d.split("=")
        box = f(label)
        focal_length = int(focal_length)
        V[box][label] = focal_length


fp = 0
for box_i, box in enumerate(V):
    for label_i, (label, focal_length) in enumerate(box.items()):
        fp += (1 + box_i) * (1 + label_i) * focal_length

print(fp)

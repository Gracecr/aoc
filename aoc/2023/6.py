from aoc.util import *

"""
number of ways you can beat the record in each race;
in this example, if you multiply these values together, you get 288 (4 * 8 * 9).
"""

D = get_data().splitlines()
D = """Time:      7  15   30
Distance:  9  40  200""".splitlines()

race_ts = [int(n) for n in D[0][len("Time: ") +1:].split()]
race_ds = [int(n) for n in D[1][len("Distance: ") +1:].split()]
race_ts = [35937366]
race_ds = [212206012011044]

def race(hold_n, tot_t):
    speed = hold_n
    dist = (tot_t - hold_n) * speed
    return dist

num_ways_to_win = []
for t, d in zip(race_ts, race_ds):
    num_ways_to_win_i = 0
    for hold_t in range(t + 1):
        if race(hold_t, t) > d:
            num_ways_to_win_i += 1
    num_ways_to_win.append(num_ways_to_win_i)

print(np.prod(num_ways_to_win))
# submit()

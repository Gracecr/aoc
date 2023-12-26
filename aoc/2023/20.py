from aoc.util import *

D = get_data().splitlines()
# D = r"""broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output""".splitlines()

SPECIAL = ["dl", "vk", "ks", "pm"]
CYCLES = defaultdict(list)

G = defaultdict(lambda: (None, None, []))
CONJ = {}
how_many_flip_flops = 0
for line in D:
    name, targets = line.split(" -> ")

    if name == "broadcaster":
        G[name] = (None, None, targets.split(", "))
    else:
        ntype, name = name[0], name[1:]
        if ntype == "%":
            G[name] = (ntype, False, targets.split(", "))
            how_many_flip_flops += 1
        else:
            G[name] = (ntype, {}, targets.split(", "))

for n, (ntype, state, _) in G.items():
    if ntype == "&":
        for n2, (_, _, targets) in G.items():
            if n in targets:
                state[n2] = False

# False = Low pulse
# True = High pulse
total_pulses = defaultdict(int)
i = 0
num_flip_flops_on_d = defaultdict(list)
for _ in range(100000):
    Q = deque([(None, "broadcaster", False)])
    i += 1
    while Q:
        caller, name, ptype = Q.popleft()

        total_pulses[ptype] += 1

        ntype, state, targets = G[name]

        if caller in SPECIAL and ptype is True:
            num_flip_flops_on_d[caller].append(i)

        if name == "broadcaster":
            for t in targets:
                Q.append((name, t, ptype))
            continue

        if ntype is None:
            continue

        if ptype is False and ntype == "%":
            state = not state
            for t in targets:
                Q.append((name, t, state))

        elif ntype == "&":
            state[caller] = ptype
            pulse_to_send = not all(state.values())
            # print(state)
            for t in targets:
                Q.append((name, t, pulse_to_send))

        G[name] = (ntype, state, targets)

# ans=# of high pulses * # of low pulses after 1000 pushes
# print(total_pulses)
# print(total_pulses[True] * total_pulses[False])
for n in sorted(num_flip_flops_on_d.keys()):
    print(n, num_flip_flops_on_d[n])

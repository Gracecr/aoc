from aoc.util import *

D = get_data().splitlines()

card_vals = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": -1,
    "Q": 12,
    "K": 13,
    "A": 14
}

hands = []
for line in D:
    hand, bid = line.split()
    bid = int(bid)
    hands.append((hand, bid))

def swap_in_jokers(hand:str):
    c = Counter(hand)
    for h in c.most_common():
        if h[0] != "J":
            return hand.replace("J", h[0])
        
    return "JJJJJ"

def calc_hand_rank(hand, j_wildcard = True):
    if j_wildcard:
        hand = swap_in_jokers(hand)

    c = Counter(hand)
    rank = max(x for x in c.values())
    
    if 3 in c.values() and 2 in c.values():
        return 3.5

    if len([x for x in c.values() if x == 2]) == 2:
        return 2.5

    return rank

def compare_hand(h1, h2):
    rank_diff = calc_hand_rank(h1[0]) - calc_hand_rank(h2[0])

    if rank_diff != 0:
        return rank_diff

    for ch1, ch2 in zip(h1[0], h2[0]):
        val = card_vals[ch1] - card_vals[ch2]
        if val != 0:
            return val
        
    return 0

hands.sort(key=functools.cmp_to_key(compare_hand))

# for h in hands:
#     print(f"{h[0]} {h[1]}")
acc = 0
for i, h in enumerate(hands):
    acc += h[1] * (i+1)
print(acc)
# submit(acc)

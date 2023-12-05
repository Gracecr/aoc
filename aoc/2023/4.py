from aoc.util import *

D = get_data().splitlines()
# D = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()
# V = get_vectors(2, diag=True)
# B = get_bounds(D)

card_points = {}
cards = {}
for line in D:
    words = line.split()
    nums = [int(n) for n in line[line.index(":")+1:line.index("|")].split()]
    lucky = [int(n) for n in line[line.index("|")+1:].split()]
    card_num = int(words[1][:-1])
    cards[card_num] = [nums, lucky]
    # acc = 0
    # for num in nums:
    #     if num in lucky:
    #         if not acc:
    #             acc = 1
    #         else:
    #             acc *=2
    # card_points[card_num] = acc

@functools.lru_cache
def eval_card(card_num: int):
    acc = 0
    for num in cards[card_num][0]:
        if num in cards[card_num][1]:
            acc += 1
    n = 1
    for i in range(card_num + 1, card_num + 1 + acc):
        n += eval_card(i)
    return n

print(sum(eval_card(card) for card in cards))
# print(num_cards)
# submit(eval_card(1) * 2)
# submit(sum(card_points.values()))
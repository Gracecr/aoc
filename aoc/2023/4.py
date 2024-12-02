from aoc.util import *

D = get_data().splitlines()
# V = get_vectors(2, diag=True)
# B = get_bounds(D)

card_points = {}
cards = {}
for line in D:
    words = line.split()
    nums = [int(n) for n in line[line.index(":") + 1 : line.index("|")].split()]
    lucky = [int(n) for n in line[line.index("|") + 1 :].split()]
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

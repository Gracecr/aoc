from aoc.util import *

d = [d for d in get_data().splitlines()]

# only 12 red cubes, 13 green cubes, and 14 blue cubes
# What is the sum of the IDs of those games?

# d = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

max_D = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
games = {}
for line in d:
    words = line.split()
    id = int(line.split()[1][:-1])
    line = line[line.index(":") + 2:]
    game_D = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for game in line.split("; "):
        for reveal in game.split(", "):
            if game_D[reveal.split()[1]] < int(reveal.split()[0]):
                game_D[reveal.split()[1]] = int(reveal.split()[0])
    games[id] = game_D

pos = []
for id, game in games.items():
    possible = True
    for color in game:
        if game[color] > max_D[color]:
            possible = False
            break
    if possible:
        pos.append(id)

print(pos)

pows = []
for id, game in games.items():
    s = 1
    for v in game.values():
        if v:
            s *= v
    pows.append(s)
submit(sum(pows))
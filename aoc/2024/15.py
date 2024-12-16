from aoc import util as u

D = u.get_data()

G, SEQ = D.split("\n\n")
G = G.replace("#", "##")
G = G.replace("O", "[]")
G = G.replace(".", "..")
G = G.replace("@", "@.")
G = [list(line.strip()) for line in G.splitlines()]
SEQ = SEQ.replace("\n", "")

DIR = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

p1 = 0
p2 = 0

for r, line in enumerate(G):
    for c, ch in enumerate(line):
        if ch == "@":
            pos = (r, c)


def print_g():
    for line in G:
        print("".join(line))


# print_g()


def can_move_box(
    box: tuple[tuple[int, int], tuple[int, int]], move: tuple[int, int]
) -> None:
    for pos in box:
        new_pos = u.addt(pos, move)
        new_pos_ch = G[new_pos[0]][new_pos[1]]
        if new_pos_ch == "#":
            return False
        if new_pos == box[1] or new_pos_ch not in "[]":
            continue

        if move in {DIR["v"], DIR["^"]}:
            if not can_move_box(
                (
                    new_pos,
                    u.addt(DIR["<"], new_pos)
                    if new_pos_ch == "]"
                    else u.addt(DIR[">"], new_pos),
                ),
                move,
            ):
                return False
        elif not can_move_box((new_pos, u.addt(move, new_pos)), move):
            return False

    return True


def move_box(box: tuple[tuple[int, int], tuple[int, int]], move: tuple[int, int]):
    for pos in box:
        new_pos = u.addt(pos, move)
        if new_pos == box[1]:
            continue
        new_pos_ch = G[new_pos[0]][new_pos[1]]
        if new_pos_ch in "[]":
            if move in {DIR["v"], DIR["^"]}:
                new_box = (
                    new_pos,
                    u.addt(DIR["<"], new_pos)
                    if new_pos_ch == "]"
                    else u.addt(DIR[">"], new_pos),
                )
            else:
                new_box = (new_pos, u.addt(move, new_pos))
            move_box(new_box, move)

    G[box[0][0]][box[0][1]] = "."
    G[box[1][0]][box[1][1]] = "."
    new_box = (u.addt(box[0], move), u.addt(box[1], move))
    if new_box[0][1] < new_box[1][1]:
        G[new_box[0][0]][new_box[0][1]] = "["
        G[new_box[1][0]][new_box[1][1]] = "]"
    else:
        G[new_box[0][0]][new_box[0][1]] = "]"
        G[new_box[1][0]][new_box[1][1]] = "["


for move in SEQ:
    new_pos = u.addt(pos, DIR[move])
    new_pos_ch = G[new_pos[0]][new_pos[1]]
    if new_pos_ch == ".":
        G[pos[0]][pos[1]] = "."
        pos = new_pos
    elif new_pos_ch in "[]":
        if move in "v^":
            box = (
                new_pos,
                u.addt(DIR["<"], new_pos)
                if new_pos_ch == "]"
                else u.addt(DIR[">"], new_pos),
            )
        else:
            box = (new_pos, u.addt(DIR[move], new_pos))
        if can_move_box(box, DIR[move]):
            move_box(box, DIR[move])
            G[pos[0]][pos[1]] = "."
            pos = new_pos
        # obs_check_ops = new_pos
        # while G[obs_check_ops[0]][obs_check_ops[1]] not in "#.":
        #     obs_check_ops = u.addt(obs_check_ops, DIR[move])
        #     if G[obs_check_ops[0]][obs_check_ops[1]] in "[]"
        # if G[obs_check_ops[0]][obs_check_ops[1]] == "#":
        #     continue
        # if G[obs_check_ops[0]][obs_check_ops[1]] == ".":
        #     G[new_pos[0]][new_pos[1]] = "@"
        #     G[pos[0]][pos[1]] = "."
        #     G[obs_check_ops[0]][obs_check_ops[1]] = "O"
        #     pos = new_pos
        #     continue
    G[pos[0]][pos[1]] = "@"
    # print_g()


for r, line in enumerate(G):
    for c, ch in enumerate(line):
        if ch == "[":
            p1 += 100 * r + c

print(p1)
print(p2)

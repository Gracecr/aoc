from aoc.util import get_data, submit  # pylint: disable=unused-import


def part_one(data: str):
    pos = [0, 0]
    rot = 0

    for line in data.splitlines():
        cmd = line[0]
        val = int(line[1:])
        if cmd == "N":
            pos[0] += val
        elif cmd == "S":
            pos[0] -= val
        elif cmd == "E":
            pos[1] += val
        elif cmd == "W":
            pos[1] -= val
        elif cmd == "R":
            rot -= val
        elif cmd == "L":
            rot += val
        elif cmd == "F":
            if rot % 360 == 0:
                pos[1] += val
            elif rot % 360 == 90:
                pos[0] += val
            elif rot % 360 == 180:
                pos[1] -= val
            elif rot % 360 == 270:
                pos[0] -= val
    return abs(pos[0]) + abs(pos[1])


def part_two(data: str):
    pos = [0, 0]
    w_pos = [1, 10]

    for line in data.splitlines():
        cmd = line[0]
        val = int(line[1:])
        if cmd == "N":
            w_pos[0] += val
        elif cmd == "S":
            w_pos[0] -= val
        elif cmd == "E":
            w_pos[1] += val
        elif cmd == "W":
            w_pos[1] -= val
        elif cmd == "R":
            if val == 90:
                w_pos = [-w_pos[1], w_pos[0]]
            elif val == 180:
                w_pos = [-w_pos[0], -w_pos[1]]
            elif val == 270:
                w_pos = [w_pos[1], -w_pos[0]]
        elif cmd == "L":
            if val == 90:
                w_pos = [w_pos[1], -w_pos[0]]
            elif val == 180:
                w_pos = [-w_pos[0], -w_pos[1]]
            elif val == 270:
                w_pos = [-w_pos[1], w_pos[0]]
        elif cmd == "F":
            pos[0] += w_pos[0] * val
            pos[1] += w_pos[1] * val
    return abs(pos[0]) + abs(pos[1])


if __name__ == "__main__":
    data_ = get_data()
    PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    # submit(PART_ONE_ANSWER)
    # submit(PART_TWO_ANSWER)

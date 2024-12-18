from aoc import util as u

D = u.get_data().splitlines()

p1 = 0
p2 = 0


A = int(u.re.findall(r"-?\d+", D[0])[0])
B = int(u.re.findall(r"-?\d+", D[1])[0])
C = int(u.re.findall(r"-?\d+", D[2])[0])
REGS = {"0": 0, "1": 1, "2": 2, "3": 3, "4": A, "5": B, "6": C}
PROG = u.re.findall(r"-?\d+", D[4])


def run_prog(regs: dict[str, int], prog: str) -> str:
    ins_ptr = 0
    output = []

    while len(prog) - ins_ptr >= 2:
        opcode = int(prog[ins_ptr])
        ins_ptr += 1
        operand = prog[ins_ptr]
        ins_ptr += 1

        # print(opcode, operand)

        if opcode == 0:
            # print(f"A = A // 2**regs[{operand}]")
            regs["4"] = regs["4"] // (2 ** regs[operand])

        elif opcode == 1:
            # print(f"B = B ^ {operand}")
            regs["5"] ^= int(operand)

        elif opcode == 2:
            # print(f"B = regs[{operand}] % 8")
            regs["5"] = regs[operand] % 8

        elif opcode == 3:
            if regs["4"] == 0:
                continue
            # print(f"jmp {operand}")
            ins_ptr = int(operand)

        elif opcode == 4:
            # print("B = B ^ C")
            regs["5"] ^= regs["6"]

        elif opcode == 5:
            # print(f"out regs[{operand}] % 8")
            output.append(regs[operand] % 8)

        elif opcode == 6:
            # print(f"B = A // 2**regs[{operand}]")
            regs["5"] = regs["4"] // (2 ** regs[operand])

        elif opcode == 7:
            # print(f"C = A // 2**regs[{operand}]")
            regs["6"] = regs["4"] // (2 ** regs[operand])
    return output


p1 = run_prog({"0": 0, "1": 1, "2": 2, "3": 3, "4": A, "5": B, "6": C}, PROG)
print(",".join(str(s) for s in p1))


prog = list(map(int, PROG))
num_digits = 9
inc = 8**num_digits
start = 0b1111000101011000001011011010110111010111101
c = 0
while num_digits < len(PROG):
    last_found = 0
    for i in range(start, 8 ** (len(PROG) + 1), inc):
        c += 1
        s = run_prog({"0": 0, "1": 1, "2": 2, "3": 3, "4": i, "5": B, "6": C}, PROG)
        if c % 10000 == 0:
            print(i)
        if s[: num_digits + 1] == prog[: num_digits + 1]:
            if s == prog:
                num_digits = len(PROG)
                break
            # print(f"Found digit #{num_digits + 1} at {i} ({bin(i)})")

print(i)

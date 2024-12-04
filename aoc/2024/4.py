from aoc import util as u

D = u.get_data().splitlines()
V = [(1, 0), (0, 1), (-1, 0), (0, -1)]
V_diag = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

p1 = 0
p2 = 0
for r in range(len(D)):
    for c in range(len(D[r])):
        ch = D[r][c]
        if ch == "X":
            for v in V_diag + V:
                pos = (r, c)
                for l in "MAS":
                    pos = u.addt(pos, v)
                    if not (0 <= pos[0] < len(D) and 0 <= pos[1] < len(D[r])):
                        break
                    if D[pos[0]][pos[1]] != l:
                        break
                else:
                    p1 += 1
        if ch == "A":
            found = 0
            for v in V_diag:
                m_pos = u.addt((r, c), v)
                s_pos = u.addt((r, c), (-v[0], -v[1]))
                if not (0 <= m_pos[0] < len(D) and 0 <= m_pos[1] < len(D[r])):
                    break
                if not (0 <= s_pos[0] < len(D) and 0 <= s_pos[1] < len(D[r])):
                    break
                if D[m_pos[0]][m_pos[1]] == "M" and D[s_pos[0]][s_pos[1]] == "S":
                    found += 1
            if found == 2:
                p2 += 1

print(p1)
print(p2)

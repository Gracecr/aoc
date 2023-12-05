import itertools
import sys

sys.path.append("C:/Users/cgrac/dev/aoc")
from util import get_data, submit  # pylint: disable=unused-import


def matches_rule(msg: str, rule: list[str], d: dict[str, str]):
    if '"' in rule:
        return msg == eval(rule)
    sub_rules = "".join(rule).split("|")
    for sub_rule in sub_rules:
        passes_rule = True
        for sub_sub_rule in sub_rule:
            if not matches_rule(msg, d[sub_sub_rule], d):
                passes_rule = False
                break
        if passes_rule:
            return True
    return None


def flatten(S):
    if isinstance(S, str):
        return S
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


def simplify(rule: list[str], rules: dict[str, list[str]]):
    if "|" in rule:
        rule1 = rule[: rule.index("|")]
        rule2 = rule[rule.index("|") + 1 :]
        return [simplify(rule1, rules), simplify(rule2, rules)]

    return rule


def gen_strs(rule, rules, visited):
    if rule in ("a", "b"):
        yield rule

    cur = ""
    for i, c in enumerate(rule):
        if c in ("a", "b"):
            cur += c
        elif isinstance(c, list):
            for c2 in gen_strs(c, rules, visited):
                yield cur + c2
        else:
            if int(c) not in visited:
                visited[int(c)] = set(gen_strs(rules[int(c)], rules, visited))
            for c2 in visited[int(c)]:
                if len(rule) == i + 1:
                    yield cur + c2
                else:
                    for c3 in gen_strs(rule[i + 1 :], rules, visited):
                        yield cur + c2 + c3
            return


def part_one(data: str):
    num_matches = 0
    rules = {}
    messages = []
    for line in data.splitlines():
        if ":" in line:
            rule_name = int(line[: line.index(":")])
            if '"' in line:
                rules[rule_name] = eval(line[line.index(":") + 1 :])
            else:
                rules[rule_name] = line[line.index(":") + 1 :].split()
        elif line:
            messages.append(line)

    simplified_rules = {}
    for rule_name, rule in rules.items():
        simplified_rules[rule_name] = simplify(rule, rules)

    sets = set()
    sets.update(gen_strs(simplified_rules[0], simplified_rules, {}))

    print(set(gen_strs(simplified_rules[42], simplified_rules, {})))

    for msg in messages:
        if msg in sets:
            num_matches += 1

    return num_matches

    # for msg in messages:
    #     for rule in simplified_rules.values():
    #         sub_rules = "".join(rule).split("|")
    #         if any(msg == sub_rule for sub_rule in sub_rules):
    #             num_matches += 1
    #             break
    # return num_matches


def part_two(data: str):
    num_matches = 0
    rules = {}
    messages = []
    for line in data.splitlines():
        if ":" in line:
            rule_name = int(line[: line.index(":")])
            if '"' in line:
                rules[rule_name] = eval(line[line.index(":") + 1 :])
            else:
                rules[rule_name] = line[line.index(":") + 1 :].split()
        elif line:
            messages.append(line)

    simplified_rules = {}
    for rule_name, rule in rules.items():
        simplified_rules[rule_name] = simplify(rule, rules)

    visited = {}
    sets = set(gen_strs(simplified_rules[0], simplified_rules, visited))
    print("done making the sets")

    rule_42_len = len(next(iter(visited[42])))
    rule_31_len = len(next(iter(visited[31])))

    for msg in messages:
        if msg in sets:
            num_matches += 1
        else:
            # Check rule 0
            if not msg[len(msg) - rule_31_len :] in visited[31]:
                continue
            found_match = False
            post_rule_42_msg = msg
            while not found_match and post_rule_42_msg[:rule_42_len] in visited[42]:
                post_rule_42_msg = post_rule_42_msg[rule_42_len:]
                rule_31_msg = post_rule_42_msg[::-1]
                rule_42_msg = post_rule_42_msg
                while (
                    rule_42_msg[:rule_42_len] in visited[42]
                    and rule_31_msg[:rule_31_len][::-1] in visited[31]
                ):
                    rule_42_msg = rule_42_msg[rule_42_len:]
                    rule_31_msg = rule_31_msg[rule_31_len:]
                if len(rule_31_msg) == len(post_rule_42_msg) / 2:
                    # Matches rule 0
                    num_matches += 1
                    found_match = True
                    print(msg)
                    break

    return num_matches


if __name__ == "__main__":
    data_ = get_data()
    # PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    # print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    # submit(PART_ONE_ANSWER)
    submit(PART_TWO_ANSWER)

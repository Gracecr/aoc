import sys

sys.path.append("C:/Users/cgrac/dev/aoc")
from util import get_data, submit  # pylint: disable=unused-import


def can_contain_shiny_gold(bag_name, rules):
    if "shiny gold" in rules[bag_name]:
        return True

    for bag in rules[bag_name]:
        if can_contain_shiny_gold(bag, rules):
            return True

    return False


def part_one(data: str):
    rules: dict[str, set[str]] = {}
    for rule in data.splitlines():
        words = rule.split()
        rule_name = words[0] + " " + words[1]
        if "no other bags" in rule:
            rules[rule_name] = set()
        else:
            # rules[rule_name] = [(int(words[4]), words[5] + " " + words[6])]
            rules[rule_name] = set([words[5] + " " + words[6]])
            while any("," in word for word in words):
                comma_index = 0
                for i, word in enumerate(words):
                    if "," in word:
                        comma_index = i
                        break
                words = words[comma_index + 1 :]
                # rules[rule_name].append((int(words[0]), words[1] + " " + words[2]))
                rules[rule_name].add(words[1] + " " + words[2])
    return sum(int(can_contain_shiny_gold(bag, rules)) for bag in rules)


def num_bags_in_bag(bag_name, rules):
    acc = 1
    for num, bag in rules[bag_name]:
        acc += num * num_bags_in_bag(bag, rules)

    return acc


def part_two(data: str):
    rules: dict[str, set[tuple[int, str]]] = {}
    for rule in data.splitlines():
        words = rule.split()
        rule_name = words[0] + " " + words[1]
        if "no other bags" in rule:
            rules[rule_name] = set()
        else:
            rules[rule_name] = set([(int(words[4]), words[5] + " " + words[6])])
            while any("," in word for word in words):
                comma_index = 0
                for i, word in enumerate(words):
                    if "," in word:
                        comma_index = i
                        break
                words = words[comma_index + 1 :]
                rules[rule_name].add((int(words[0]), words[1] + " " + words[2]))
    return num_bags_in_bag("shiny gold", rules) - 1


if __name__ == "__main__":
    data_ = get_data()
    PART_ONE_ANSWER = part_one(data_)
    PART_TWO_ANSWER = part_two(data_)

    print(f"{PART_ONE_ANSWER=}")
    print(f"\n{PART_TWO_ANSWER=}")

    # submit(PART_ONE_ANSWER)
    submit(PART_TWO_ANSWER)

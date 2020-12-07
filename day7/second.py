import re

rules = open("input.txt").readlines()


def find_interior_bags(bag):
    line = ""
    for rule in rules:
        if rule[0:rule.index("bag") - 1] == bag:
            line = rule
            break

    interior_bags = 1
    if "other" in line:
        return interior_bags

    line = line[line.index("bag") + 3:]
    while "bag" in line:
        next_bag_color = re.search(r"((\w+) ){2}(?=bag)", line)[0][:-1]
        amount = int(re.search(r"\d+", line)[0])
        interior_bags += find_interior_bags(next_bag_color) * amount
        line = line[line.index("bag") + 3:]
    return interior_bags


print(find_interior_bags("shiny gold") - 1)

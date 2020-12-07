rules = open("input.txt").readlines()


def find_exterior_bags(bag):
    outside_bags = set()
    for rule in rules:
        if bag in rule and rule[:rule.index("bag") - 1] != bag:
            outside_bags.add(rule[:rule.index("bag") - 1])
            outside_bags = outside_bags.union(find_exterior_bags(rule[:rule.index("bag") - 1]))
    return outside_bags


print(len(find_exterior_bags("shiny gold")))

import re
from collections import defaultdict
# Let's make a rule graph from these. 


def parse_rules(rules):
    return [tuple(map(int, i.split("|"))) for i in rules.split("\n")]

def parse_updates(updates):
    return [tuple(map(int, i.split(","))) for i in updates.split("\n")]

def create_graphs(parsed_rules):
    graph = defaultdict(set)
    reversed_graph = defaultdict(set)
    for before, after in parsed_rules:
        graph[before].add(after)
        reversed_graph[after].add(before)
    return graph, reversed_graph


input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

updates = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

if __name__ == "__main__":
    parsed_rules = parse_rules(input)
    x, y = create_graphs(parsed_rules)
    print(x)
    parsed_updates = parse_updates(updates)        

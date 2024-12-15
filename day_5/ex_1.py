import os
import re
import requests
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()
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


input_test = """47|53
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

updates_test = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def get_middle_value(tuple):
    mid_idx = len(tuple) // 2
    return tuple[mid_idx]

def mapping_function(rule_dict, update_tuple):
    # need to check for all the pairs. 
    for i in range(len(update_tuple)):
        for j in range(i + 1, len(update_tuple)):
            page_1, page_2 = update_tuple[i], update_tuple[j]
            if page_1 in rule_dict[page_2]:
                return False
    return get_middle_value(update_tuple)

# Helper function

def get_lists_from_aoc(cookie):

# You'll need to include your session cookie
    cookies = {
        'session': cookie  # Get this from your browser after logging in
    }

    response = requests.get(
        'https://adventofcode.com/2024/day/5/input',
        cookies=cookies
    )

    return response.text.strip()

if __name__ == "__main__":
    cookie = os.environ.get("cookie")
    total_input = get_lists_from_aoc(cookie=cookie)
    input, updates = total_input.split("\n\n")
    parsed_rules = parse_rules(input)
    print(len(parsed_rules))
    x, y = create_graphs(parsed_rules)
    # print(x)
    parsed_updates = parse_updates(updates)
    print(len(parsed_updates))
    valid = [mapping_function(x, j) for j in parsed_updates]
    print(sum(valid))

# ADD THE MIDDLE PAGE NUMBER
    

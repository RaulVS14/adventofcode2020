import re

from helpers.helpers import read_file

TARGET_BAG = "shiny gold"

def total_occurrence_of_type_of_bag(rules, param):
    keys = [param]
    seen = []
    while keys:
        new_keys = []
        for rule in rules:
            for key in keys:
                if key in rules[rule].keys():
                    new_keys.append(rule)
                    if rule not in seen:
                        seen.append(rule)
        keys = new_keys
    return len(seen)


def recursive_total_occurrence(rules, param):
    visited = set()
    for rule, contents in rules.items():
        if param in contents:
            visited.add(rule)
            visited.update(recursive_total_occurrence(rules, rule))
    return visited


def get_total_of_bags_that_fit_shiny_gold_bag(file_name):
    file = read_file(file_name)
    rules = get_rules_map(file)
    return len(recursive_total_occurrence(rules, TARGET_BAG)) or total_occurrence_of_type_of_bag(rules, TARGET_BAG)


def get_rules_map(file):
    rule_dict = {}
    for line in file:
        rule = re.findall(r'([0-9]?)[ ]?(\w* \w*) bag[s]?', line)
        main_bag = rule.pop(0)

        if main_bag[1] not in rule_dict:
            rule_dict[main_bag[1]] = {}

        for inner in rule:
            if inner[1] != 'no other':
                rule_dict[main_bag[1]][inner[1]] = int(inner[0])
    return rule_dict


def total_amount_of_bags_inside_type_of_bag(rules, param):
    ans = 0
    for y in rules[param]:
        value = (1 + total_amount_of_bags_inside_type_of_bag(rules, y))
        ans += rules[param][y] * value
    return ans


def get_total_amount_of_bags_inside_shiny_bag(file_name):
    file = read_file(file_name)
    rules = get_rules_map(file)
    return total_amount_of_bags_inside_type_of_bag(rules, TARGET_BAG)

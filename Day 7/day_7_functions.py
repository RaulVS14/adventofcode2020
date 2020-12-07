import re

from helpers.helpers import read_file


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


def get_total_of_bags_that_fit_shiny_gold_bag(file_name):
    file = read_file(file_name)
    rules = get_rules_map(file)
    return total_occurrence_of_type_of_bag(rules, "shiny gold")


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


def section_2_function(file_name):
    file = read_file(file_name)
    return file

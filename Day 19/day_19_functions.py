import re

from helpers.helpers import read_file


def find_suitable_messages_for_rule_0(rules):
    rule_0 = rules["0"]
    return False


def find_total_of_messages_that_match_rule_0(file_name):
    file = read_file(file_name)
    rules, messages = process_file(file)
    potential_messages = find_suitable_messages_for_rule_0(rules)
    return file


def process_file(file):
    rules ={}
    messages =[]
    for line in file:
        regex_line = re.match(r'^(?P<key>\d*)\: "?(?P<value>[a-z0-9\| ]*)"?$', line)
        if regex_line:
            key = regex_line.group("key")
            value = regex_line.group("value")
            rules[key] = value.split()
        elif line == "":
            continue
        else:
            messages.append(line)
    return rules, messages


def section_2_function(file_name):
    file = read_file(file_name)
    return file

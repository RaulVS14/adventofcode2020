import re

from helpers.helpers import read_file


def find_total_of_messages_that_match_rule_0(file_name):
    file = read_file(file_name)
    rules, messages = process_file(file)
    return file


def process_file(file):
    rules ={}
    message =[]
    for line in file:
        regex_line = re.match(r'^(?P<key>\d*)\: "?(?P<value>[a-z0-9\| ]*)"?$', line)
        if regex_line:
            key = regex_line.group("key")
            value = regex_line.group("value")
            rules[key] = value.split()
        elif line == "":
            continue
        else:
            message.append(line)
    return rules, message


def section_2_function(file_name):
    file = read_file(file_name)
    return file

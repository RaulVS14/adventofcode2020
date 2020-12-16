import re

from helpers.helpers import read_file


def process_file(file):
    row = 0
    data = {}
    data["rules"] = {}
    key_word = False
    while row < len(file):
        row_match = re.match(r'(?P<key>^[a-z ]*): (?P<rule1>\d*\-\d*) or (?P<rule2>\d*\-\d*)', file[row])
        if row_match:
            data["rules"][row_match.group('key')] = [row_match.group('rule1').split("-"),
                                                     row_match.group('rule2').split("-")]
        elif not file[row]:
            row += 1
            continue
        elif re.match(r'(?P<key>^[a-z ]*):', file[row]):
            match_row_key = re.match(r'(?P<key>^[a-z ]*):', file[row])
            key_word = match_row_key.group('key')
            data[key_word] = []
        else:
            data[key_word].append(file[row].split(","))
        row += 1
    return data


def check_field(field, rules):
    for rule in rules:
        for rule_part in rules[rule]:
            if int(rule_part[0]) <= int(field) <= int(rule_part[1]):
                return True
    return False


def find_in_valid_fields(rules_and_tickets):
    rules = rules_and_tickets["rules"]
    tickets = rules_and_tickets["nearby tickets"]
    invalid_fields = []
    for ticket in tickets:
        for field in ticket:
            if not check_field(field, rules):
                invalid_fields.append(int(field))
    return invalid_fields


def get_sum_of_invalid_field_numbers(file_name):
    file = read_file(file_name)
    rules_and_tickets = process_file(file)
    list_of_invalid_fields = find_in_valid_fields(rules_and_tickets)
    return sum(list_of_invalid_fields)


def remove_invalid_tickets(rules_and_tickets):
    rules = rules_and_tickets["rules"]
    tickets = rules_and_tickets["nearby tickets"]
    new_tickets = []
    for index in range(len(tickets)):
        valid_ticket = True
        for field in tickets[index]:
            if not check_field(field, rules):
                valid_ticket = False
                break
        if valid_ticket:
            new_tickets.append(tickets[index])
    rules_and_tickets["nearby tickets"] = new_tickets[:]
    return rules_and_tickets


def check_field_for_label(field, current_rule):
    for rule_part in current_rule:
        if int(rule_part[0]) <= int(field) <= int(rule_part[1]):
            return True
    return False


def find_field_labels(rules_and_tickets):
    rules = rules_and_tickets["rules"]
    tickets = rules_and_tickets["nearby tickets"]
    field_labels = {}
    index = 0
    while index < len(rules):
        rules_set = []
        for rule in rules:
            current_rule_name, current_rule = rule, rules[rule]
            result = True
            for ticket in tickets:
                result = result and check_field_for_label(ticket[index], current_rule)
            if result:
                rules_set.append(current_rule_name)
        field_labels[index] = rules_set
        index += 1
    return field_labels


def process_labels_dict(labels_dict):
    label_list_dict = {}
    while len(label_list_dict.keys()) != len(labels_dict.keys()):
        for i in labels_dict:
            if len(labels_dict[i]) == 1:
                current_label = labels_dict[i][0]
                label_list_dict[str(i)] = current_label
                labels_dict = remove_processed_labels_from_repeating_label_dict_lists(current_label, i, labels_dict)
    return label_list_dict


def remove_processed_labels_from_repeating_label_dict_lists(current_label, i, labels_dict):
    for j in labels_dict:
        if i != j and current_label in labels_dict[j]:
            labels_dict[j].pop(labels_dict[j].index(current_label))
    return labels_dict


def multiplie_departed_field_numbers(labels_list, ticket):
    multiplication = 1
    for i in range(len(labels_list)):
        if "departure" in labels_list[i]:
            multiplication *= int(ticket[int(i)])
    return multiplication


def get_multiplied_departure_field_numbers_from_your_ticket(file_name):
    labels_list, your_ticket = get_order_label_list(file_name)
    return multiplie_departed_field_numbers(labels_list, your_ticket)


def organize_labels(indexed_label_dict):
    organize = []
    while len(organize) < len(indexed_label_dict.keys()):
        organize.append(indexed_label_dict[str(len(organize))])
    return organize


def get_order_label_list(file_name):
    file = read_file(file_name)
    rules_and_tickets = process_file(file)
    filtered_tickets = remove_invalid_tickets(rules_and_tickets)
    labels_dict = find_field_labels(filtered_tickets)
    indexed_label_dict = process_labels_dict(labels_dict)
    organized_labels_list = organize_labels(indexed_label_dict)
    return organized_labels_list, rules_and_tickets["your ticket"][0]

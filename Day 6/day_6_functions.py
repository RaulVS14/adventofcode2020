from helpers.helpers import read_file


def get_sum_of_forms_yes_answers(file_name):
    file = read_file(file_name)
    groups = get_groups_unique_answers(file)
    return get_groups_yes_answers_sum(groups)


def get_groups_yes_answers_sum(groups):
    groups_sum = 0
    for group in groups:
        groups_sum += sum_group_unique_yes_answers(group)
    return groups_sum


def sum_group_unique_yes_answers(group):
    unique_group_answers_list = []
    for i in group:
        unique_group_answers_list += i
    return len(list(set(unique_group_answers_list)))


def get_groups_unique_answers(file):
    groups = []
    group = []
    for i, entry in enumerate(file):
        if entry == "":
            groups.append(group)
            group = []
        elif i == len(file) - 1:
            groups.append(group)
            group.append(list(set(entry)))
        else:
            group.append(list(set(entry)))
    return groups


def get_sum_of_groups_common_yes_answers(file_name):
    file = read_file(file_name)
    groups = get_groups_unique_answers(file)
    return get_groups_common_yes_answers_sum(groups)


def get_groups_common_yes_answers_sum(groups):
    groups_sum = 0
    for group in groups:
        groups_sum += sum_group_common_yes_answers(group)
    return groups_sum


def sum_group_common_yes_answers(group):
    list_of_common_answers = False
    for person in group:
        if not list_of_common_answers and not isinstance(list_of_common_answers, list):
            list_of_common_answers = person
        list_of_common_answers = list(set(list_of_common_answers) & set(person))
    return len(list_of_common_answers)

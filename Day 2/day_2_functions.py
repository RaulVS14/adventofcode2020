import re

from helpers.helpers import read_file


def get_letter_count_in_word(word, letter):
    letter_count = 0
    for i in word:
        if i == letter:
            letter_count += 1
    return letter_count


def handle_line(line):
    line_groups = re.match(r"(?P<min>\d{1,3})-(?P<max>\d{1,3}) (?P<letter>\w): (?P<password>\w*)", line)
    first_number = int(line_groups.group("min"))
    second_number = int(line_groups.group("max"))
    letter = line_groups.group("letter")
    word = line_groups.group("password")
    return first_number, second_number, letter, word


def check_password_letter_count(line):
    at_least, at_most, required_letter, password = handle_line(line)
    count = get_letter_count_in_word(password, required_letter)
    return count >= at_least and count <= at_most


def check_password_letter_position(line):
    position_first, position_second, required_letter, password = handle_line(line)
    letter_position_first = password[position_first -1] if position_first - 1 < len(password) else False
    letter_position_second = password[position_second - 1] if position_second - 1 < len(password) else False
    return (letter_position_first == required_letter) != (letter_position_second == required_letter)


def get_file_correct_password_count_letter_count_based(file):
    correct_password_count = 0
    for i in file:
        if check_password_letter_count(i):
            correct_password_count += 1
    return correct_password_count


def get_file_correct_password_count_letter_position_based(file):
    correct_password_count = 0
    for i in file:
        if check_password_letter_position(i):
            correct_password_count += 1
    return correct_password_count


def find_correct_passwords_from_file(file_name, type=False):
    file = read_file(file_name, str)
    if type == "count":
        return get_file_correct_password_count_letter_count_based(file)
    elif type == "position":
        return get_file_correct_password_count_letter_position_based(file)
    else:
        return False

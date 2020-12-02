import re

from helpers.helpers import read_file


def get_letter_count_in_word(word, letter):
    letter_count = 0
    for i in word:
        if i == letter:
            letter_count += 1
    return letter_count


def check_password(line):
    line_groups = re.match(r"(?P<min>\d{1,3})-(?P<max>\d{1,3}) (?P<letter>\w): (?P<password>\w*)", line)
    at_least = int(line_groups.group("min"))
    at_most = int(line_groups.group("max"))
    required_letter = line_groups.group("letter")
    password = line_groups.group("password")
    count = get_letter_count_in_word(password, required_letter)
    return count >= at_least and count <= at_most


def get_file_correct_password_count(file):
    correct_password_count = 0
    for i in file:
        if check_password(i):
            correct_password_count += 1
    return correct_password_count


def find_correct_passwords_from_file(file_name):
    file = read_file(file_name, str)
    return get_file_correct_password_count(file)

from helpers.helpers import read_file


def get_last_spoken(numbers, last_step):
    result = []
    step = len(numbers)
    while len(result) < 2:
        step = step - 1
        if numbers[step] == last_step:
            result.append(step)
    return result[0] - result[1]


def find_nth_number(starting_numbers, pos_in_sequence):
    numbers = {}
    current_step = 0
    number_to_add = starting_numbers[0]
    while current_step < pos_in_sequence:
        prev = number_to_add
        if current_step < len(starting_numbers):
            number_to_add = starting_numbers[current_step]
        elif prev not in numbers:
            number_to_add = 0
        else:
            number_to_add = current_step - 1 - numbers[prev]
        numbers[prev] = current_step - 1
        current_step += 1
    return number_to_add


def find_2020th_number_in_sequence(file_name):
    file = read_file(file_name)
    starting_numbers = [int(x) for x in file[0].split(',')]
    return find_nth_number(starting_numbers, 2020)


def find_30000000th_number_in_sequence(file_name):
    file = read_file(file_name)
    starting_numbers = [int(x) for x in file[0].split(',')]
    return find_nth_number(starting_numbers, 30000000)

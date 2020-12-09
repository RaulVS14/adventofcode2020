from helpers.helpers import read_file


def find_first_invalid(number_list, preamble):
    for i in range(preamble, len(number_list)):
        if not check_number(number_list[i], number_list[i - preamble:i]):
            return number_list[i]


def check_number(number, preamble_list):
    for i in range(len(preamble_list)):
        for j in range(len(preamble_list)):
            if i == j:
                continue

            if preamble_list[i] + preamble_list[j] == number:
                return True
    return False


def find_invalid_number(file_name, preamble):
    file = read_file(file_name, int)
    return find_first_invalid(file, preamble)


def find_encryption_weakness(file_name, preamble):
    file = read_file(file_name, int)
    value = find_first_invalid(file, preamble)
    sum_list = find_contiguous_number_list(file, value)
    return get_sum_of_min_max(sum_list)


def get_sum_of_min_max(sum_numbers):
    return min(sum_numbers) + max(sum_numbers)


def find_contiguous_number_list(file, number):
    for i in range(len(file)):
        current_visited = []
        for j in range(i, len(file)):
            current_visited.append(file[j])
            if sum(current_visited) == number:
                return current_visited
    return []
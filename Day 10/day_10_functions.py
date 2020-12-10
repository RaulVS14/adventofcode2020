from helpers.helpers import read_file


def calculate_difference_multiplication(file_name):
    file = read_file(file_name, int)
    diff_of_1, diff_of_3 = get_diff_lists(file)
    return diff_of_1 * diff_of_3


def get_diff_lists(file):
    adapter_list = file[:]
    n_1_difference = 0
    index = 0
    n_3_difference = 0
    current_element = 0
    while index < len(adapter_list) + 1:
        item_index = 0
        if current_element + 1 in adapter_list:
            item_index = adapter_list.index(current_element + 1)
            n_1_difference += 1
        elif current_element + 3 in adapter_list:
            item_index = adapter_list.index(current_element + 3)
            n_3_difference += 1
        elif current_element + 2 in adapter_list:
            item_index = adapter_list.index(current_element + 2)
        current_element = adapter_list[item_index]
        index += 1

    if index == len(adapter_list) + 1:
        n_3_difference += 1
    return n_1_difference, n_3_difference


def find_adapter_combinations(file, i, mem):
    answer = 0
    if i == len(file) - 1:
        return 1
    if i in mem:
        return mem[i]
    for j in range(i + 1, len(file)):
        if file[j] - file[i] <= 3:
            answer += find_adapter_combinations(file, j, mem)
    mem[i] = answer
    return answer


def get_all_adapter_combinations(file_name):
    file = read_file(file_name, int)
    file.append(0) # Include beginning in the array
    file.append(max(file) + 3) # Include ending in the array
    sorted_adapters = sorted(file) # sort the file for the combination finding
    return find_adapter_combinations(sorted_adapters, 0, {})

from helpers.helpers import read_file


def check_sum_2020(*args):
    return sum(args) == 2020


def get_multiple_of_2_nr_that_sum_2020(input, ):
    multiple = 0
    input_file = read_file("input.txt", int)
    for i in range(len(input_file)):
        current_element = input_file[i]
        for j in range(i, len(input_file)):
            current_2nd_element = input_file[j]
            if check_sum_2020(current_element, current_2nd_element):
                multiple = current_element * current_2nd_element
    return multiple


def get_multiple_of_3_nr_that_sum_2020(input):
    multiple = 0
    input_file = read_file("input.txt", int)
    for i in range(len(input_file)):
        current_element = input_file[i]
        for j in range(i, len(input_file)):
            current_2nd_element = input_file[j]
            for k in range(j, len(input_file)):
                current_3rd_element = input_file[k]
                if check_sum_2020(current_element, current_2nd_element, current_3rd_element):
                    multiple = current_element * current_2nd_element * current_3rd_element
    return multiple
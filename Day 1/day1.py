from day_1_functions import get_multiple_of_2_nr_that_sum_2020, get_multiple_of_3_nr_that_sum_2020
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(514579 == get_multiple_of_2_nr_that_sum_2020('test_input.txt'), 1, 1))
    print(output_result(get_multiple_of_2_nr_that_sum_2020('input.txt'), 1, 1))

    # Part 2
    print(output_test_result(241861950 == get_multiple_of_3_nr_that_sum_2020('test_input.txt'), 1, 2))
    print(output_result(get_multiple_of_3_nr_that_sum_2020('input.txt'), 1, 2))

from day_6_functions import get_sum_of_forms_yes_answers, get_sum_of_groups_common_yes_answers
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(11 == get_sum_of_forms_yes_answers("test_input.txt"), 6, 1))
    print(output_result(get_sum_of_forms_yes_answers("input.txt"), 6, 1))

    # Part 2
    print(get_sum_of_groups_common_yes_answers("test_input.txt"))
    print(output_test_result(6 == get_sum_of_groups_common_yes_answers("test_input.txt"), 6, 2))
    print(output_result(get_sum_of_groups_common_yes_answers("input.txt"), 6, 2))

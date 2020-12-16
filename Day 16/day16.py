from day_16_functions import get_sum_of_invalid_field_numbers, get_multiplied_departure_field_numbers_from_your_ticket, \
    get_order_label_list
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(71 == get_sum_of_invalid_field_numbers("test_input.txt"), 16, 1))
    print(output_result(get_sum_of_invalid_field_numbers("input.txt"), 16, 1))

    # Part 2
    print(output_test_result(['row', 'class', 'seat'] == get_order_label_list("test_input.txt")[0], 16, 2.1))
    print(output_test_result(['row', 'class', 'seat'] == get_order_label_list("test_input2.txt")[0], 16, 2.2))
    print(output_result(get_multiplied_departure_field_numbers_from_your_ticket("input.txt"), 16, 2))

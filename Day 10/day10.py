from day_10_functions import calculate_difference_multiplication, get_all_adapter_combinations
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(35 == calculate_difference_multiplication("test_input.txt"), 10, 1))
    print(output_test_result(220 == calculate_difference_multiplication("test_input_2.txt"), 10, 1))
    print(output_result(calculate_difference_multiplication("input.txt"), 10, 1))

    # Part 2
    print(output_test_result(8 == get_all_adapter_combinations("test_input.txt"), 10, 2))
    print(output_test_result(19208 == get_all_adapter_combinations("test_input_2.txt"), 10, 2))
    print(output_result(get_all_adapter_combinations("input.txt"), 10, 2))

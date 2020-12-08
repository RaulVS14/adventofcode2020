from day_8_functions import get_accumulator_value_from_boot_code, find_accumulator_value_in_fixed_system
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(5 == get_accumulator_value_from_boot_code("test_input.txt"), 8, 1))
    print(output_result(get_accumulator_value_from_boot_code("input.txt"), 8, 1))

    # Part 2
    print(output_test_result(8 == find_accumulator_value_in_fixed_system("test_input.txt"), 8, 2))
    print(output_result(find_accumulator_value_in_fixed_system("input.txt"), 8, 2))

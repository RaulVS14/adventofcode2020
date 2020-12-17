from day_17_functions import get_count_of_active_cubes_after_6_runs, section_2_function
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(112 == get_count_of_active_cubes_after_6_runs("test_input.txt"), 17, 1))
    print(output_result(get_count_of_active_cubes_after_6_runs("input.txt"), 17, 1))

    # Part 2
    print(output_test_result(848 == section_2_function("test_input.txt"), 17, 2))
    print(output_result(section_2_function("input.txt"), 17, 2))

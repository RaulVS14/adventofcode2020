from day_14_functions import sum_program_memory_values_after_running, sum_memory_values_after_running_memory_decoder
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(165 == sum_program_memory_values_after_running("test_input.txt"), 14, 1))
    print(output_result(sum_program_memory_values_after_running("input.txt"), 14, 1))

    # Part 2
    print(output_test_result(208 == sum_memory_values_after_running_memory_decoder("test_input2.txt"), 14, 2))
    print(output_result(sum_memory_values_after_running_memory_decoder("input.txt"), 14, 2))

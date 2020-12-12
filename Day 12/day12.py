from day_12_functions import find_mathattan_distance_for_planned_instructions, find_mathattan_distance_for_travelled_instructions
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(25 == find_mathattan_distance_for_planned_instructions("test_input.txt"), 12, 1))
    print(output_result(find_mathattan_distance_for_planned_instructions("input.txt"), 12, 1))

    # Part 2
    print(output_test_result(286 == find_mathattan_distance_for_travelled_instructions("test_input.txt"), 12, 2))
    print(output_result(find_mathattan_distance_for_travelled_instructions("input.txt"), 12, 2))

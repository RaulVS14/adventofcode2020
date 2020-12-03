from day_3_functions import get_encountered_trees_count, get_multiplication_of_trees_from_different_paths
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(7 == get_encountered_trees_count("test_input.txt"), 3, 1))
    print(output_result(get_encountered_trees_count("input.txt"), 3, 1))

    # Part 2
    print(output_test_result(336 == get_multiplication_of_trees_from_different_paths("test_input.txt"), 3, 2))
    print(output_result(get_multiplication_of_trees_from_different_paths("input.txt"), 3, 2))

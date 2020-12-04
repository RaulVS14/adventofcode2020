from day_4_functions import validate_passports
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(2 == validate_passports("test_input.txt"),4,1))
    print(output_result(validate_passports("input.txt"), 4, 1))

    # Part 2
    # print(output_test_result(336 == get_multiplication_of_trees_from_different_paths("test_input.txt"), 3, 2))
    # print(output_result(get_multiplication_of_trees_from_different_paths("input.txt"), 3, 2))

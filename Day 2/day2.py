from day_2_functions import find_correct_passwords_from_file
from helpers.helpers import output_result, output_test_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(2 == find_correct_passwords_from_file("test_input.txt", type="count"), 2, 1))
    print(output_result(find_correct_passwords_from_file("input.txt", type="count"), 2, 1))

    # Part 2
    print(output_test_result(1 == find_correct_passwords_from_file("test_input.txt", type="position"), 2, 2))
    print(output_result(find_correct_passwords_from_file("input.txt", type="position"), 2, 2))

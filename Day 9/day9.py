from day_9_functions import find_invalid_number, find_encryption_weakness
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(127 == find_invalid_number("test_input.txt", 5), 9, 1))
    print(output_result(find_invalid_number("input.txt", 25), 9, 1))

    # Part 2
    print(output_test_result(62 == find_encryption_weakness("test_input.txt", 5), 9, 2))
    print(output_result(find_encryption_weakness("input.txt", 25), 9, 2))

from day_4_functions import validate_passports, secure_validate_passports
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(2 == validate_passports("test_input.txt"),4,1))
    print(output_result(validate_passports("input.txt"), 4, 1))

    # Part 2
    print(output_test_result(0 == secure_validate_passports("test_input_invalid.txt"), 4, 2))
    print(output_test_result(0 < secure_validate_passports("test_input_valid.txt"), 4, 2))
    print(output_result(secure_validate_passports("input.txt"), 4, 2))

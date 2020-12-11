from day_11_functions import count_occupied_seats, count_again_occupied_seats
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(37 == count_occupied_seats("test_input.txt"), 11, 1))
    print(output_result(count_occupied_seats("input.txt"), 11, 1))

    # Part 2
    print(output_test_result(26 == count_again_occupied_seats("test_input.txt"), 11, 2))
    print(output_result(count_again_occupied_seats("input.txt"), 11, 2))

from helpers.helpers import output_test_result, output_result
from day_5_functions import get_boarding_passes, get_heighest_seat_id

if __name__ == "__main__":
    test_result = [[70, 7, 567], [14, 7, 119], [102, 4, 820]]
    # Part 1
    print(output_test_result(test_result == get_boarding_passes("test_input.txt"), 5, 1))
    print(output_result(get_heighest_seat_id("input.txt"), 5, 1))

from day_15_functions import find_2020th_number_in_sequence, find_30000000th_number_in_sequence
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(436 == find_2020th_number_in_sequence("test_input.txt"), 15, 1.1))
    print(output_test_result(1 == find_2020th_number_in_sequence("test_input1.txt"), 15, 1.2))
    print(output_test_result(10 == find_2020th_number_in_sequence("test_input2.txt"), 15, 1.3))
    print(output_test_result(27 == find_2020th_number_in_sequence("test_input3.txt"), 15, 1.4))
    print(output_test_result(78 == find_2020th_number_in_sequence("test_input4.txt"), 15, 1.5))
    print(output_test_result(438 == find_2020th_number_in_sequence("test_input5.txt"), 15, 1.6))
    print(output_test_result(1836 == find_2020th_number_in_sequence("test_input6.txt"), 15, 1.7))
    print(output_result(find_2020th_number_in_sequence("input.txt"), 15, 1))

    # Part 2
    print(output_test_result(175594 == find_30000000th_number_in_sequence("test_input.txt"), 15, 2.1))
    print(output_test_result(2578 == find_30000000th_number_in_sequence("test_input1.txt"), 15, 2.2))
    print(output_test_result(3544142 == find_30000000th_number_in_sequence("test_input2.txt"), 15, 2.3))
    print(output_test_result(261214 == find_30000000th_number_in_sequence("test_input3.txt"), 15, 2.4))
    print(output_test_result(6895259 == find_30000000th_number_in_sequence("test_input4.txt"), 15, 2.5))
    print(output_test_result(18 == find_30000000th_number_in_sequence("test_input5.txt"), 15, 2.6))
    print(output_test_result(362 == find_30000000th_number_in_sequence("test_input6.txt"), 15, 2.7))
    print(output_result(find_30000000th_number_in_sequence("input.txt"), 15, 2))

from day_19_functions import find_total_of_messages_that_match_rule_0, section_2_function
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(2 == find_total_of_messages_that_match_rule_0("test_input.txt"), 19, 1))
    print(output_result(find_total_of_messages_that_match_rule_0("input.txt"), 19, 1))

    # Part 2
    print(output_test_result('result' == section_2_function("test_input.txt"), 19, 2))
    print(output_result(section_2_function("input.txt"), 19, 2))

from day_7_functions import get_total_of_bags_that_fit_shiny_gold_bag, get_total_amount_of_bags_inside_shiny_bag
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(4 == get_total_of_bags_that_fit_shiny_gold_bag("test_input.txt"), 7, 1))
    print(output_result(get_total_of_bags_that_fit_shiny_gold_bag("input.txt"), 7, 1))

    # Part 2
    print(output_test_result(32 == get_total_amount_of_bags_inside_shiny_bag("test_input.txt"), 7, 2))
    print(output_test_result(126 == get_total_amount_of_bags_inside_shiny_bag("test_input_2.txt"), 7, 2))
    print(output_result(get_total_amount_of_bags_inside_shiny_bag("input.txt"), 7, 2))

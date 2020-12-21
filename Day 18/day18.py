from day_18_functions import solve_homework_problems_equal_precendence, solve_homework_problems_addition_precendence
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(71 == solve_homework_problems_equal_precendence("test_input.txt"), 18, 1.1))
    print(output_test_result(51 == solve_homework_problems_equal_precendence("test_input1.txt"), 18, 1.11))
    print(output_test_result(26 == solve_homework_problems_equal_precendence("test_input2.txt"), 18, 1.2))
    print(output_test_result(437 == solve_homework_problems_equal_precendence("test_input3.txt"), 18, 1.3))
    print(output_test_result(12240 == solve_homework_problems_equal_precendence("test_input4.txt"), 18, 1.4))
    print(output_test_result(13632 == solve_homework_problems_equal_precendence("test_input5.txt"), 18, 1.5))
    print(output_result(solve_homework_problems_equal_precendence("input.txt"), 18, 1))

    # Part 2
    print(output_test_result(231 == solve_homework_problems_addition_precendence("test_input.txt"), 18, 2.1))
    print(output_test_result(51 == solve_homework_problems_addition_precendence("test_input1.txt"), 18, 2.11))
    print(output_test_result(46 == solve_homework_problems_addition_precendence("test_input2.txt"), 18, 2.2))
    print(output_test_result(1445 == solve_homework_problems_addition_precendence("test_input3.txt"), 18, 12.3))
    print(output_test_result(669060 == solve_homework_problems_addition_precendence("test_input4.txt"), 18, 2.4))
    print(output_test_result(23340 == solve_homework_problems_addition_precendence("test_input5.txt"), 18, 2.5))
    print(output_result(solve_homework_problems_addition_precendence("input.txt"), 18, 2))

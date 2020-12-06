from day_6_functions import section_1_function, section_2_function
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
	# Part 1
	print(output_test_result('result' == section_1_function("test_input.txt"), 6, 1))
	print(output_result(section_1_function("input.txt"), 6, 1))

	# Part 2
	print(output_test_result('result' == section_2_function("test_input.txt"), 6, 1))
	print(output_result(section_2_function("input.txt"), 6, 1))

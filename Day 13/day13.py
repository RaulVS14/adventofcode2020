from day_13_functions import get_earliest_bus_id_multiplied_by_wait_minutes, \
    get_earliest_timestamp_when_busses_depart_1_min_apart
from helpers.helpers import output_test_result, output_result

if __name__ == "__main__":
    # Part 1
    print(output_test_result(295 == get_earliest_bus_id_multiplied_by_wait_minutes("test_input.txt"), 13, 1))
    print(output_result(get_earliest_bus_id_multiplied_by_wait_minutes("input.txt"), 13, 1))

    # Part 2
    print(output_test_result(1068781 == get_earliest_timestamp_when_busses_depart_1_min_apart("test_input.txt"), 13, 2))
    print(output_result(get_earliest_timestamp_when_busses_depart_1_min_apart("input.txt"), 13, 2))

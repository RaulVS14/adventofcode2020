from helpers.helpers import read_file


def get_earliest_bus_id_multiplied_by_wait_minutes(file_name):
    file = read_file(file_name)
    earliest_time = int(file[0])
    busses = get_bus_array(file[1])
    bus_id, minutes = find_bus_id(earliest_time, busses)
    return bus_id * minutes


def get_bus_array(bus_file_line):
    return [int(bus) for bus in bus_file_line.split(",") if bus != "x"]


def find_bus_id(earliest_time, busses):
    nearest_bus_id = 0
    nearest_arrival_time = earliest_time + min(busses)
    for bus in busses:
        minutes_since_the_bus_last_arrived = earliest_time % bus
        next_bus_arrival = earliest_time - minutes_since_the_bus_last_arrived + bus
        if next_bus_arrival < nearest_arrival_time:
            nearest_bus_id = bus
            nearest_arrival_time = next_bus_arrival
    return nearest_bus_id, nearest_arrival_time - earliest_time


def get_earliest_timestamp_when_busses_depart_1_min_apart(file_name):
    file = read_file(file_name)
    busses = file[1].split(',')
    return process_busses(busses)


def process_busses(busses):
    earliest_time = 0  # since busses should depart after each other we can count the beginning 0 for each search
    step = 1  # initial step size
    for index, bus in enumerate(busses):
        if bus != 'x':
            # Like previously, we are trying to find timestamp for each bus,
            # by incrementing each next bus time with multiplication of all the previous busses
            while (earliest_time + index) % int(bus) != 0:
                earliest_time += step
            step *= int(bus)
    return earliest_time

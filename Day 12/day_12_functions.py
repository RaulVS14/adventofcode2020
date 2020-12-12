import re
from math import cos, sin, radians, ceil

from helpers.helpers import read_file

INITIAL_FACING_DIRECTION = 'E'
DIRECTIONAL_MAP = {
    "N": 1,
    "E": 1,
    "S": -1,
    "W": -1,
}


def find_mathattan_distance_for_planned_instructions(file_name):
    file = read_file(file_name)
    latitude, longitude = process_navigation(file)
    return manhattan_distance(latitude, longitude)  # n/s e/w


def process_navigation(file):
    facing_direction = INITIAL_FACING_DIRECTION
    latitude = 0
    longitude = 0
    for line in file:
        instr_amount, instr_direction = process_line_into_instruction(line)
        if instr_direction == "F":
            latitude, longitude = process_directional_movement(instr_amount, facing_direction, latitude, longitude)
        elif instr_direction in ["R", "L"]:
            map_directions = list(DIRECTIONAL_MAP.keys())
            current_facing_position = map_directions.index(facing_direction)
            position_change = instr_amount / 90
            if instr_direction == "L":
                position_change = -1 * position_change
            facing_direction = map_directions[int((current_facing_position + position_change) % len(map_directions))]
        else:
            latitude, longitude = process_directional_movement(instr_amount, instr_direction, latitude, longitude)

    return latitude, longitude


def process_directional_movement(instr_amount, instr_direction, latitude, longitude):
    if instr_direction in ["N", "S"]:
        latitude += DIRECTIONAL_MAP[instr_direction] * instr_amount
    elif instr_direction in ["E", "W"]:
        longitude += DIRECTIONAL_MAP[instr_direction] * instr_amount
    return latitude, longitude


def process_line_into_instruction(line):
    instruction = re.match(r'(\w)(\d+)', line)
    instr_direction = instruction.group(1)
    instr_amount = int(instruction.group(2))
    return instr_amount, instr_direction


def manhattan_distance(latitude, longitude):
    return abs(latitude) + abs(longitude)


def process_travel(file):
    ship_latitude = 0
    ship_longitude = 0
    waypoint_latitude = 1
    waypoint_longitude = 10
    for line in file:
        instr_amount, instr_direction = process_line_into_instruction(line)
        if instr_direction == "F":
            ship_latitude += waypoint_latitude * instr_amount
            ship_longitude += waypoint_longitude * instr_amount
        elif instr_direction in ["R", "L"]:
            if instr_direction == "R":
                instr_amount = -1 * instr_amount
            current_longitude_position = waypoint_longitude
            current_latitude_position = waypoint_latitude
            rotate_angle_rad = radians(instr_amount)
            waypoint_longitude = round(
                current_longitude_position * cos(rotate_angle_rad) - current_latitude_position * sin(rotate_angle_rad))
            waypoint_latitude = round(
                + current_longitude_position * sin(rotate_angle_rad) + current_latitude_position * cos(
                    rotate_angle_rad))
        else:
            waypoint_latitude, waypoint_longitude = process_directional_movement(instr_amount, instr_direction,
                                                                                 waypoint_latitude, waypoint_longitude)

    return ship_latitude, ship_longitude


def find_mathattan_distance_for_travelled_instructions(file_name):
    file = read_file(file_name)
    latitude, longitude = process_travel(file)
    return manhattan_distance(latitude, longitude)  # n/s e/w

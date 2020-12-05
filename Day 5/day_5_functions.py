from helpers.helpers import read_file
from math import ceil, floor


def calc_seat_id(row, column):
    return row * 8 + column


def get_heighest_seat_id(file_name):
    result = 0
    boarding_passes = get_boarding_passes(file_name)
    for i in boarding_passes:
        if i[2] > result:
            result = i[2]
    return result


def get_boarding_passes(file_name):
    file = read_file(file_name)
    boarding_list = []
    for i in file:
        row_part = get_row(i[:-3])
        column_part = get_column(i[-3:])
        boarding_pass = [row_part, column_part, calc_seat_id(row_part, column_part)]
        boarding_list.append(boarding_pass)
    return boarding_list


def get_row(row_string):
    limits = [0, 127]
    last_index = 0
    for char in row_string:
        if char == "B":
            last_index = 1
            limits = [limits[1] - floor((limits[1] - limits[0]) / 2), limits[1]]
        elif "F":
            last_index = 0
            limits = [limits[0], limits[1] - ceil((limits[1] - limits[0]) / 2)]
    return limits[last_index]


def get_column(column_string):
    limits = [0, 7]
    last_index = 0
    for char in column_string:
        if char == "R":
            last_index = 1
            limits = [limits[1] - floor((limits[1] - limits[0]) / 2), limits[1]]
        else:
            limits = [limits[0], limits[1] - ceil((limits[1] - limits[0]) / 2)]
            last_index = 0
    return limits[last_index]

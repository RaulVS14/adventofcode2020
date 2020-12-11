import copy

from helpers.helpers import read_file

OCCUPIED = "#"
VACANT = "L"


def count_occupied_seats(file_name):
    file = read_file(file_name)
    return process_seats(file, check_adjacent_seats, 4)


def get_seats_count(seats):
    count = 0
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == OCCUPIED:
                count += 1
    return count


def process_seats(file, validation_method, tolerance):
    updating = True
    count = 0
    new_seats = file.copy()
    while updating:
        updating, count, new_seats = handle_processing(new_seats, validation_method, tolerance)
    return count


def handle_processing(input_seats, validation_method, tolerance_level):
    seats = input_seats.copy()
    new_seats = []
    count = 0
    update_state = False
    for i in range(len(seats)):
        new_seats.append([])
        for j in range(len(seats[i])):
            current_seat = seats[i][j]
            new_seats[i].append(current_seat)
            occupied_count = validation_method(seats, i, j)
            new_seats[i][j] = get_replacement(current_seat, occupied_count, tolerance_level)
            if new_seats[i][j] == OCCUPIED:
                count += 1
            if current_seat != new_seats[i][j]:
                update_state = True
    return update_state, count, new_seats


def get_replacement(current_seat, occupied_count, tolerance_level):
    if current_seat == VACANT and occupied_count == 0:
        replacement = current_seat.replace(VACANT, OCCUPIED)
    elif current_seat == OCCUPIED and occupied_count >= tolerance_level:
        replacement = current_seat.replace(OCCUPIED, VACANT)
    else:
        replacement = current_seat
    return replacement


def check_adjacent_seats(seats, row, column):
    occupied_count = 0
    for i in range(row - 1, row + 2):
        if 0 <= i < len(seats):
            occupied_count = handle_column(seats, row, column, occupied_count, i)
    return occupied_count


def handle_column(seats, row, column, count, row_iterator):
    for column_iterator in range(column - 1, column + 2):
        if row_iterator == row and column_iterator == column:
            continue
        if (0 <= column_iterator < len(seats[row_iterator])) and seats[row_iterator][column_iterator] == OCCUPIED:
            count += 1
    return count


def check_directional_seats(seats, row, column):
    direction_dict = [-1, 0, 1]
    occupied_count = 0
    for direction_y in [-1, 0, 1]:
        for direction_x in direction_dict:
            if direction_y == 0 and direction_x == 0:
                continue
            occupied_count += find_directional_seat(seats, row, column, direction_y, direction_x)
    return occupied_count


def find_directional_seat(seats, row, column, direction_y, direction_x):
    y = row
    x = column
    while (0 <= y + direction_y < len(seats) and 0 <= x + direction_x < len(seats[0])):
        x += direction_x
        y += direction_y
        if seats[y][x] == "L":
            return 0

        if seats[y][x] == OCCUPIED:
            return 1
    return 0


def count_again_occupied_seats(file_name):
    file = read_file(file_name)
    return process_seats(file, check_directional_seats, 5)

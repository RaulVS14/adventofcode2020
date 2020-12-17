from helpers.helpers import read_file


def get_count_of_active_cubes_after_6_runs(file_name):
    dimensions = 3
    file = read_file(file_name)
    active_elements_set = coordinates_of_active_elements(file)
    return find_max_active_cube_count(active_elements_set, dimensions)


def coordinates_of_active_elements(file):
    layout = set()
    for row, line in enumerate(file):
        for column, char in enumerate(line):
            if char == '#':
                coordinates = (row, column)
                for _ in range(2, 4):
                    coordinates += (0,)
                layout.add(coordinates)
    return layout


def min_space_for_given_coordinate_axis(layout, axis):
    return min(active_element[axis] for active_element in layout) - 1


def max_space_for_given_coordinate_axis(layout, axis):
    return max(active_element[axis] for active_element in layout) + 2


def find_max_active_cube_count(layout, dimensions):
    current_active_set = layout
    process = 0
    while process < 6:
        new_active_set = set()
        for x in range(min_space_for_given_coordinate_axis(current_active_set, 0),
                       max_space_for_given_coordinate_axis(current_active_set, 0)):
            for y in range(min_space_for_given_coordinate_axis(current_active_set, 1),
                           max_space_for_given_coordinate_axis(current_active_set, 1)):
                for z in range(min_space_for_given_coordinate_axis(current_active_set, 2),
                               max_space_for_given_coordinate_axis(current_active_set, 2)):
                    for t in get_dimension_range(current_active_set, dimensions):
                        neighbour_count = find_nearest_active_neighbor_count(current_active_set, x, y, z, t)
                        new_active_set = update_active_set(current_active_set, neighbour_count, new_active_set, x, y,
                                                           z, t)
        current_active_set = new_active_set
        process += 1
    return len(current_active_set)


def get_dimension_range(current_active_set, dimensions):
    if dimensions == 4:
        return range(min_space_for_given_coordinate_axis(current_active_set, 3), max_space_for_given_coordinate_axis(
            current_active_set, 3))
    return [0]


def update_active_set(current_active_set, neighbour_count, new_active_set, x, y, z, t):
    cube_coordinates = (x, y, z, t)
    if cube_coordinates not in current_active_set and neighbour_count == 3:
        new_active_set.add(cube_coordinates)
    if cube_coordinates in current_active_set and neighbour_count in [2, 3]:
        new_active_set.add(cube_coordinates)
    return new_active_set


def find_nearest_active_neighbor_count(current_active_set, x, y, z, t):
    neighbour_count = 0
    for neighbor_x in [-1, 0, 1]:
        for neighbor_y in [-1, 0, 1]:
            for neighbor_z in [-1, 0, 1]:
                for neighbor_t in [-1, 0, 1]:
                    neighbour_count = increment_neighbor_count_if_active(current_active_set, neighbor_t, neighbor_x,
                                                                         neighbor_y, neighbor_z, neighbour_count, t, x,
                                                                         y, z)
    return neighbour_count


def increment_neighbor_count_if_active(current_active_set, neighbor_t, neighbor_x, neighbor_y, neighbor_z,
                                       neighbour_count, t, x, y, z):
    neighbor_coordinates = (x + neighbor_x, y + neighbor_y, z + neighbor_z, t + neighbor_t)
    check_if_self_coordinates = neighbor_x != 0 or neighbor_y != 0 or neighbor_z != 0 or neighbor_t != 0
    if check_if_self_coordinates and neighbor_coordinates in current_active_set:
        neighbour_count += 1
    return neighbour_count


def get_count_of_active_cubes_in_4_dimensions_after_6_runs(file_name):
    dimensions = 4
    file = read_file(file_name)
    active_elements_set = coordinates_of_active_elements(file)
    return find_max_active_cube_count(active_elements_set, dimensions)

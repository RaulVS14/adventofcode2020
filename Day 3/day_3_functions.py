from helpers.helpers import read_file


def decend_slope(file, right=3, left=1):
    elements = []
    while len(elements) * left != len(file) - 1:
        current_row = len(elements)
        y = current_row * left + left
        row = file[y]
        x = right * (current_row + 1) % (len(row))
        element = row[x]
        elements.append(element)
    return elements


def get_encountered_trees_count(file_name):
    file = read_file(file_name)
    return get_tree_count_from_path(decend_slope(file))


def get_tree_count_from_path(path):
    return path.count("#")


def get_multiplication_of_trees_from_different_paths(file_name):
    file = read_file(file_name)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    multiplied_trees = 1
    for i in slopes:
        slope_trees = get_tree_count_from_path(decend_slope(file, i[0], i[1]))
        multiplied_trees *= slope_trees
    return multiplied_trees

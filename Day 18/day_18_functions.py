from helpers.helpers import read_file


def find_matching_parenthesis_index(expression):
    unclosed = 0
    for i, char in enumerate(expression):
        if char == '(':
            unclosed += 1
        elif char == ')':
            unclosed -= 1
            if unclosed == 0:
                return i
    return False


def calc(param, param1, operator):
    if operator == "+":
        return int(param) + int(param1)
    else:
        return int(param) * int(param1)


def process_expression(expression):
    if len(expression) == 1:
        return int(expression[0])
    elif expression[0] == '(':
        closing_parenthesis_index = find_matching_parenthesis_index(expression)
        enclosed_expression = expression[1: closing_parenthesis_index]
        result_of_enclosed_expression = str(process_precedence_expressions(enclosed_expression))
        new_expression = [result_of_enclosed_expression] + expression[closing_parenthesis_index + 1:]
        return process_expression(new_expression)
    elif expression[2] == '(':
        closing_parenthesis_index = find_matching_parenthesis_index(expression)
        enclosed_expression = expression[3: closing_parenthesis_index]
        result_of_enclosed_expression = str(process_precedence_expressions(enclosed_expression))
        new_expression = expression[:2] + [result_of_enclosed_expression] + expression[closing_parenthesis_index + 1:]
        return process_expression(new_expression)
    else:
        result = calc(int(expression[0]), expression[2], expression[1])
        new_expression = [str(result)] + expression[3:]
        return process_expression(new_expression)


def process_precedence_expressions(expression):
    if len(expression) == 1:
        return int(expression[0])
    elif expression[0] == '(':
        closing_parenthesis_index = find_matching_parenthesis_index(expression)
        enclosed_expression = expression[1: closing_parenthesis_index]
        result_of_enclosed_expression = str(process_precedence_expressions(enclosed_expression))
        new_expression = [result_of_enclosed_expression] + expression[closing_parenthesis_index + 1:]
        return process_precedence_expressions(new_expression)
    elif expression[2] == '(':
        closing_parenthesis_index = find_matching_parenthesis_index(expression)
        enclosed_expression = expression[3: closing_parenthesis_index]
        result_of_enclosed_expression = str(process_precedence_expressions(enclosed_expression))
        new_expression = expression[:2] + [result_of_enclosed_expression] + expression[closing_parenthesis_index + 1:]
        return process_precedence_expressions(new_expression)
    else:
        elem1 = expression[0]
        elem2 = expression[2]
        operator = expression[1]
        if operator == "+":
            new_expression = [str(calc(elem1, elem2, operator))] + expression[3:]
            return process_precedence_expressions(new_expression)
        else:
            calculation_result = process_precedence_expressions(expression[2:])
            return calc(elem1, str(calculation_result), operator)


def solve_all_expressions(file, calculation):
    result = 0
    for line in file:
        line_expression_list = list(line.replace(' ', ""))
        result += calculation(line_expression_list)
    return result


def solve_homework_problems_equal_precendence(file_name):
    file = read_file(file_name)
    return solve_all_expressions(file, process_expression)


def solve_homework_problems_addition_precendence(file_name):
    file = read_file(file_name)
    return solve_all_expressions(file, process_precedence_expressions)

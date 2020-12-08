import copy
import re

from helpers.helpers import read_file


def get_accumulator_value_from_boot_code(file_name):
    file = read_file(file_name)
    instructions = get_instructions(file)
    acc_result, _ = process_instructions(instructions)
    return acc_result


def process_instructions(instructions):
    acc = 0
    processed = []
    current = 0
    complete_instruction_found = False
    while current not in processed:
        if len(instructions) == current:
            complete_instruction_found = True
            break

        cmd, value = instructions[current]
        processed.append(current)
        if cmd == "acc":
            acc += value
            current += 1
        elif cmd == "jmp":
            current += value
        else:
            current += 1
    return acc, complete_instruction_found


def get_instructions(file):
    instructions = []
    for line in file:
        line_regex = re.match(r'^(\w*) ([\+\-])(\d*)$', line)
        value = int(line_regex.group(3)) if line_regex.group(2) == "+" else -int(line_regex.group(3))
        instructions.append([line_regex.group(1), value])
    return instructions


def find_accumulator_value_in_fixed_system(file_name):
    file = read_file(file_name)
    instructions = get_instructions(file)
    return find_correct_instructions_acc_value(instructions)


def find_correct_instructions_acc_value(instructions):
    acc = 0
    for i in range(len(instructions)):
        if instructions[i][0] not in ["jmp", "nop"]:
            continue
        new_instructions = copy.deepcopy(instructions)
        if instructions[i][0] == "jmp":
            new_instructions[i][0] = "nop"
        elif instructions[i][0] == "nop":
            new_instructions[i][0] = "jmp"

        acc, end_of_instruction_reached = process_instructions(instructions=new_instructions)

        if end_of_instruction_reached:
            break
    return acc

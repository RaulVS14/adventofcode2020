import re

from helpers.helpers import read_file


def apply_mask(bin_val, current_mask):
    for i in range(len(bin_val)):
        if current_mask[i] != "X":
            bin_val = bin_val[:i] + current_mask[i] + bin_val[i + 1:]
    return bin_val


def process_commands(file):
    program_memory = {}
    current_mask = ""
    for line in file:
        if "mask" in line:
            current_mask = line.split(" ")[-1]
        else:
            mem_pos, mem_val = get_mem_pos_and_value(line)
            bin_val = format(mem_val, f'0{len(current_mask)}b')
            masked_value = apply_mask(bin_val, current_mask)
            program_memory[mem_pos] = masked_value
    return program_memory


def get_mem_pos_and_value(line):
    mem_line = line.split(" ")
    mem_val = int(mem_line[-1])
    mem_pos_list = re.search(r'mem\[(\d*)\]', mem_line[0])
    mem_pos = int(mem_pos_list.group(1))
    return mem_pos, mem_val


def sum_program_values(program):
    sum_of_program = 0
    for key in program:
        sum_of_program += int(program[key], 2)
    return sum_of_program


def sum_program_memory_values_after_running(file_name):
    file = read_file(file_name)
    program = process_commands(file)
    return sum_program_values(program)


def get_masked_memory_position(memory_pos_bin_val, current_mask):
    for i in range(len(memory_pos_bin_val)):
        if current_mask[i] != "0":
            memory_pos_bin_val = memory_pos_bin_val[:i] + current_mask[i] + memory_pos_bin_val[i + 1:]
    return memory_pos_bin_val


def get_memory_positions(masked_memory_pos_bin_val):
    position_list = []
    for i in range(len(masked_memory_pos_bin_val)):
        if masked_memory_pos_bin_val[i] == "X":
            position_list += get_memory_positions(masked_memory_pos_bin_val[:i] + "0" + masked_memory_pos_bin_val[i + 1:])
            position_list += get_memory_positions(masked_memory_pos_bin_val[:i] + "1" + masked_memory_pos_bin_val[i + 1:])
            return position_list
    return [masked_memory_pos_bin_val]

def process_memory_decoder(file):
    memory = {}
    current_mask = ""
    for line in file:
        if "mask" in line:
            current_mask = line.split(" ")[-1]
        else:
            memory_pos, memory_val = get_mem_pos_and_value(line)
            memory_pos_bin_val = format(memory_pos, f'0{len(current_mask)}b')
            masked_memory_pos_bin_val = get_masked_memory_position(memory_pos_bin_val, current_mask)
            list_of_memory_positions = get_memory_positions(masked_memory_pos_bin_val)
            for i in list_of_memory_positions:
                memory[i] = format(memory_val, f'0{len(current_mask)}b')
    return memory


def sum_memory_values_after_running_memory_decoder(file_name):
    file = read_file(file_name)
    memory = process_memory_decoder(file)
    return sum_program_values(memory)

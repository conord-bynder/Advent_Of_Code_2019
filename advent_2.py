#!/usr/bin/python
import argparse
import pdb

parser = argparse.ArgumentParser(description='')
parser.add_argument(
    '--input', default='.', type=str,
    help="Module input data")

def add(index, program_list):
    noun = program_list[index + 1]
    verb = program_list[index + 2]
    addend_1 = program_list[noun]
    addend_2 = program_list[verb]

    destination = program_list[index + 3]
    program_list[destination] = addend_1 + addend_2
    

def multiply(index, program_list):
    noun = program_list[index + 1]
    verb = program_list[index + 2]
    factor_1 = program_list[noun]
    factor_2 = program_list[verb]
    destination = program_list[index + 3]
    program_list[destination] = factor_1 * factor_2

def process_opcode_program(program_list):
    i = 0
    while True:
        opcode = program_list[i]
        if opcode == 99:
            break
        if opcode == 1:
            add(i, program_list)
        if opcode == 2:
            multiply(i, program_list)
        i += 4
    return program_list


def find_inputs_for_output(original_list, number):
    for x in range(100):
        for y in range(100):
            program_list = original_list.copy()
            program_list[1] = x
            program_list[2] = y
            result = process_opcode_program(program_list)
            if result[0] == number:
                return result
            y+=1
        x+=1


def main():
    args = parser.parse_args()
    input_data = []
    with open(args.input, "r") as f:
        input_data = f.readline()

    original_list = [int(item) for item in input_data.split(',')]
    answer = find_inputs_for_output(original_list, 19690720)
    print(100 * answer[1] + answer[2])

if __name__ == "__main__":
    main()

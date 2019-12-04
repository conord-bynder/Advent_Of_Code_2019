#!/usr/bin/python
import argparse
import pdb

parser = argparse.ArgumentParser(description='')
parser.add_argument(
    '--input', default='.', type=str,
    help="Module input data")
def main():
    args = parser.parse_args()
    input_data = []
    with open(args.input, "r") as f:
        input_data = f.readline()
    # TO DO
    #original_list = [int(item) for item in input_data.split(',')]
    #answer = find_inputs_for_output(original_list, 19690720)
    #print(100 * answer[1] + answer[2])

if __name__ == "__main__":
    main()

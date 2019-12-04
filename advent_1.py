#!/usr/bin/python
import argparse
import logging
import pdb

log = logging.getLogger(__name__)
parser = argparse.ArgumentParser(description='')
parser.add_argument(
    '--input', default='.', type=str,
    help="Module input data")


def find_module_necessary_fuel(mass_of_fuel):
    module_fuel = (mass_of_fuel//3) - 2
    if module_fuel > 0:
        extra_fuel = find_module_necessary_fuel(module_fuel)
        return module_fuel + extra_fuel
    elif module_fuel <= 0 :
        return 0


def main():
    args = parser.parse_args()
    #pdb.set_trace()
    input_data = []
    with open(args.input, "r") as f:
        input_data = f.readlines()

    result = 0

    #print(find_module_necessary_fuel(100756))
    for module in input_data:
        try:
            result = result + int(find_module_necessary_fuel(int(module)))
        except Exception:
            pdb.set_trace()
    print(result)
    log.info("Program done")

if __name__ == "__main__":
    main()

"""
Advent of Code 2019
Day 1: The Tyranny of the Rocket Equation

PART TWO

Gist:
- Given part one measures
- Fuel requires fuel too
- If fuel is now negative amount, then treat as zero
- Find the new fuel amount

"""

import math

INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"

def calculate_fuel(mass):
    """ Calculates fuel """
    new_mass = math.floor(mass / 3) - 2
    if new_mass <= 0:
        return 0
    return new_mass + calculate_fuel(new_mass)

def run_program():
    """ Finds solution """
    output_file = open(OUTPUT_FILE_NAME, "w")
    sum_of_fuel = 0

    with open(INPUT_FILE_NAME, "rt") as input_file:
        input_line = input_file.readline()
        while input_line:
            input_line = input_line.strip()
            fuel = calculate_fuel(int(input_line.strip()))
            sum_of_fuel += fuel
            output_file.write(str(fuel) + "\n")
            input_line = input_file.readline()

    output_file.close()

    print("output.txt generated")
    print("sum of fuel: " + str(sum_of_fuel))

run_program()

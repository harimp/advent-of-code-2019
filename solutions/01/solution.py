"""
Advent of Code 2019
Day 1: The Tyranny of the Rocket Equation

Gist:
- Input file is given
- Fuel is calculated as floor(distance / 3) - 2
- Find the sum of fuel

"""

import math

def calculate_fuel(distance):
    """ Calculates fuel as fuel = floor(distance/3)-2 """
    return math.floor(distance / 3) - 2

INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"

output_file = open(OUTPUT_FILE_NAME, "w")
sum_of_fuel = 0

with open(INPUT_FILE_NAME, "rt") as fp:
    input_line = fp.readline()
    while input_line:
        input_line = input_line.strip()
        fuel = calculate_fuel(int(input_line.strip()))
        sum_of_fuel += fuel
        output_file.write(str(fuel) + "\n")
        input_line = fp.readline()

output_file.close()

print("output.txt generated")
print("sum of fuel: " + str(sum_of_fuel))

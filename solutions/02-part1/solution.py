"""
Advent of Code 2019
Day 2: 1202 Program Alarm

PART ONE

Gist:
- List of integers given
- Opcode 1: <pos1> <pos2> <dest> addition
- Opcode 2: <pos1> <pos2> <dest> multiplication
- Calculate the values and find pos 0 value

"""

INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"
SEP = ","

def calculate(sequence):
    """ Runs the opcodes """
    i = 0
    while i < len(sequence):
        opcode = sequence[i]
        if opcode == 99:
            break
        elif opcode == 1:
            pos_first = sequence[i+1]
            pos_second = sequence[i+2]
            destination = sequence[i+3]
            sequence[destination] = sequence[pos_first] + sequence[pos_second]
            i += 4
        elif opcode == 2:
            pos_first = sequence[i+1]
            pos_second = sequence[i+2]
            destination = sequence[i+3]
            sequence[destination] = sequence[pos_first] * sequence[pos_second]
            i += 4
        else:
            raise ValueError('Unknown opcode')
    return sequence

def find_solution():
    """ Finds solution """
    input_file = open(INPUT_FILE_NAME)
    output_file = open(OUTPUT_FILE_NAME, "w")

    sequence = [int(x) for x in input_file.readline().split(SEP)]

    # custom behaviour in the problem (1202)
    sequence[1] = 12
    sequence[2] = 2

    final_sequence = calculate(sequence)

    input_file.close()

    output_file.write(SEP.join(map(str, final_sequence)))

    output_file.close()

    print("output.txt generated")
    print("pos 0 value: " + str(final_sequence[0]))

find_solution()

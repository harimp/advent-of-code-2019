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
TARGET = 19690720

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
            return [i]
    return sequence

def iterate_noun_verb(original_sequence):
    """ Brute force through 0 - 99 for noun and verb """
    noun = 0
    while noun <= 99:
        verb = 0
        while verb <= 99:
            sequence = original_sequence.copy()
            sequence[1] = noun
            sequence[2] = verb

            final_sequence = calculate(sequence)
            if final_sequence[0] == TARGET:
                return (noun, verb, final_sequence)
            verb += 1
        noun += 1

    raise ValueError('No answer found')


def find_solution():
    """ Finds solution """
    input_file = open(INPUT_FILE_NAME)
    output_file = open(OUTPUT_FILE_NAME, "w")

    original_sequence = [int(x) for x in input_file.readline().split(SEP)]
    (noun, verb, final_sequence) = iterate_noun_verb(original_sequence)

    output_file.write(SEP.join(map(str, final_sequence)))

    input_file.close()
    output_file.close()

    print("output.txt generated")
    print("answer: " + str(100*noun + verb))

find_solution()

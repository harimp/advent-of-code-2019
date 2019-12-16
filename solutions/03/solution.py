"""
Advent of Code 2019
Day 3: Crossed Wires

Gist:
- Wires description is given in input file
- Wires start from center (0,0)
- Find Manhattan distance for closest intersection

"""

INPUT_FILE_NAME = 'input.txt'

def get_wire_desc():
    """ read file and get wire descriptions """
    with open(INPUT_FILE_NAME, "rt") as input_file:
        first_wire = input_file.readline().split(',')
        second_wire = input_file.readline().split(',')
    return [first_wire, second_wire]

def direction_increments(direction):
    """ get increments on direction """
    if direction == 'U':
        return (0, 1)
    if direction == 'D':
        return (0, -1)
    if direction == 'L':
        return (-1, 0)
    if direction == 'R':
        return (1, 0)
    raise ValueError('What direction is this?!?', direction)

def get_wire_points(wire):
    """ get point tuples from wire """
    current_x = 0
    current_y = 0
    points = set()
    for segment in wire:
        direction = segment[0]
        increments = direction_increments(direction)

        length = int(segment[1:])
        for _ in range(length):
            current_x += increments[0]
            current_y += increments[1]
            points.add((current_x, current_y))
    return points

def distance(point):
    """ find the manhattan distance """
    return abs(point[0]) + abs(point[1])

def solve():
    """ Find solution """
    # get wires
    wires = get_wire_desc()
    point_sets = (get_wire_points(wires[0]), get_wire_points(wires[1]))
    intersections = point_sets[0].intersection(point_sets[1])
    distances = sorted([distance(point) for point in list(intersections)])
    print(intersections)
    print(distances)

solve()

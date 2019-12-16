"""
Advent of Code 2019
Day 3: Crossed Wires

Gist:
- Wires description is given in input file
- Wires start from center (0,0)
- Find the closest wire distance to an intersection

"""

import math

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
    points = []
    for segment in wire:
        direction = segment[0]
        increments = direction_increments(direction)

        length = int(segment[1:])
        for _ in range(length):
            current_x += increments[0]
            current_y += increments[1]
            points.append((current_x, current_y))
    return points

def get_wire_distance(wire, target_point):
    """ get distance through wire """
    distance = 0
    for point in wire:
        distance += 1
        if point == target_point:
            return distance
    return math.inf

def get_intersection_wire_distance(wire, intersections):
    """ get wire distance for intersections """
    return [get_wire_distance(wire, point) for point in intersections]

def get_shortest_wire_distance(wires, intersections):
    """ got tired of writing these """
    wd_one = get_intersection_wire_distance(wires[0], intersections)
    wd_two = get_intersection_wire_distance(wires[1], intersections)
    wd_combined = []
    for i in range(len(wd_one)):
        wd_combined.append(wd_one[i] + wd_two[i])
    return sorted(wd_combined)[0]

def solve():
    """ Find solution """
    # get wires
    wires = get_wire_desc()
    point_sets = (get_wire_points(wires[0]), get_wire_points(wires[1]))

    intersections = set(point_sets[0]).intersection(set(point_sets[1]))
    print(get_shortest_wire_distance(point_sets, intersections))

solve()

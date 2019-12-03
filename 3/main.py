import sys
from collections import namedtuple
from typing import List


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), "r") as file:
        return file.read()


def input_by_lines() -> List:
    return read_input().splitlines()


Point = namedtuple('Point', "x y")


def move_right(start: Point, length: int):
    for j in range(1, length + 1):
        yield Point(start.x, start.y + j)


def move_up(start: Point, length: int):
    for j in range(1, length + 1):
        yield Point(start.x + j, start.y)


def move_left(start: Point, length: int):
    for j in range(1, length + 1):
        yield Point(start.x, start.y - j)


def move_down(start: Point, length: int):
    for j in range(1, length + 1):
        yield Point(start.x - j, start.y)


def intersection(first: List, second: List) -> List:
    return list(set(first).intersection(set(second)))


def fewest_combined_steps(steps: List):
    sum = sys.maxsize
    for i in steps:
        if sum > coords[0].index(i) + coords[1].index(i):
            sum = coords[0].index(i) + coords[1].index(i)
    return sum + 2


if __name__ == '__main__':
    lines = input_by_lines()
    first_wire = lines[0].split(",")
    second_wire = lines[1].split(",")
    coords = []
    wires = (first_wire, second_wire)
    for wire in wires:
        steps = []
        for i in wire:
            length = int(i[1:])
            direction = i[0]
            start = Point(0, 0) if len(steps) == 0 else steps[-1]
            if direction == 'R':
                steps += move_right(start, length)
            if direction == 'U':
                steps += move_up(start, length)
            if direction == 'L':
                steps += move_left(start, length)
            if direction == 'D':
                steps += move_down(start, length)

        coords.append(steps)

    common_points = intersection(coords[0], coords[1])

    print("fewest steps:", fewest_combined_steps(common_points))

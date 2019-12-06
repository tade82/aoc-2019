import itertools
import sys
from typing import List, Iterable


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), "r") as file:
        return file.read()


def input_by_lines() -> List:
    return read_input().splitlines()


def input_by_words(sep=None) -> Iterable:
    lines = read_input().splitlines()
    for line in lines:
        for word in line.split(sep=sep):
            yield int(word)


def toMap(lines, separator):
    map = {}
    for line in lines:
        tmp = line.split(separator)
        map[tmp[1]] = tmp[0]
    return map


if __name__ == '__main__':
    lines = input_by_lines()
    orbits = toMap(lines, ')')
    path = {}
    for object, center in orbits.items():
        path_to_com = []
        c = center
        while c != 'COM':
            path_to_com.append(c)
            c = orbits[c]
        path_to_com.append(center)
        path[object] = path_to_com

    for i, j in itertools.product(range(len(path['YOU'])), range(len(path['SAN']))):
        if path['YOU'][i] == path['SAN'][j]:
            sys.exit(f"result {i + j}")

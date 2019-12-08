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


if __name__ == '__main__':

    print(f"")

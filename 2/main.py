import itertools
import sys
from typing import Iterable


def read_input():
    with open((__file__.rstrip("main.py")+"input.txt"), "r") as file:
        return file.read()


def input_by_words(sep=None) -> Iterable:
    lines = read_input().splitlines()
    for line in lines:
        for word in line.split(sep=sep):
            yield int(word)


if __name__ == '__main__':
    for a, b in itertools.product(range(1, 99), range(1, 99)):
        input = list(input_by_words(","))
        input[1] = a
        input[2] = b
        i = 0
        while input[i] != 99:
            if input[i] == 1:
                input[input[i + 3]] = input[input[i + 1]] + input[input[i + 2]]
            if input[i] == 2:
                input[input[i + 3]] = input[input[i + 1]] * input[input[i + 2]]
            i += 4

        if input[0] == 19690720:
            print(f"noun: {a} verb: {b}")
            result = 100 * a + b
            sys.exit([f"result: {result}"])

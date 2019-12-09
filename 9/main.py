from typing import List, Iterable
import asyncio


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


def parameters(instruction):
    p1 = instructions[index(instruction, "p1", instruction["pointer"] + 1)]

    p2 = instructions[index(instruction, "p2", instruction["pointer"] + 2)]

    return p1, p2


def index(instruction, px, i):
    p_value = instructions[i]
    if instruction.get(px) == 0:
        return p_value
    elif instruction.get(px) == 2:
        return p_value + instruction["rb"]
    else:
        return i


def set_i(i, value):
    if i >= len(instructions):
        instructions.extend(0 for _ in range(len(instructions), i + 1))
    instructions[i] = value


def adds(instruction):
    p1, p2 = parameters(instruction)
    i = index(instruction, 'p3', instruction["pointer"] + 3)
    set_i(i, p1 + p2)
    return 4


def multiplies(instruction):
    p1, p2 = parameters(instruction)
    i = index(instruction, 'p3', instruction["pointer"] + 3)
    set_i(i, p1 * p2)
    return 4


def jump_if_true(instruction):
    p1, p2 = parameters(instruction)
    return p2 if p1 else instruction["pointer"] + 3


def jump_if_false(instruction):
    p1, p2 = parameters(instruction)
    return p2 if not p1 else instruction["pointer"] + 3


def less_than(instruction):
    p1, p2 = parameters(instruction)
    i = index(instruction, 'p3', instruction["pointer"] + 3)
    set_i(i, 1 if p1 < p2 else 0)
    return 4


def equals(instruction):
    p1, p2 = parameters(instruction)
    i = index(instruction, 'p3', instruction["pointer"] + 3)
    set_i(i, 1 if p1 == p2 else 0)
    return 4


def amplify(input):
    pointer = 0
    relative_base = 0
    while instructions[pointer] != 99:
        opcode = instructions[pointer] % 100
        instruction = {
            "rb": relative_base,
            "pointer": pointer,
            "opcode": opcode,
            "p1": 0 if instructions[pointer] < 100 else int(str(instructions[pointer])[-3]),
            "p2": 0 if instructions[pointer] < 1000 else int(str(instructions[pointer])[-4]),
            "p3": 0 if instructions[pointer] < 10000 else int(str(instructions[pointer])[-5])
        }
        if opcode == 1:
            pointer += adds(instruction)
        elif opcode == 2:
            pointer += multiplies(instruction)
        elif opcode == 3:
            if instruction.get("p1") == 0:
                p1 = instructions[pointer + 1]
            elif instruction.get("p1") == 2:
                p1 = instructions[pointer + 1] + relative_base
            else:
                p1 = pointer + 1
            instructions[p1] = input
            pointer += 2
        elif opcode == 4:
            if instruction.get("p1") == 0:
                p1 = instructions[instructions[pointer + 1]]
            elif instruction.get("p1") == 2:
                p1 = instructions[instructions[pointer + 1] + relative_base]
            else:
                p1 = instructions[pointer + 1]
            print(" result", p1)
            pointer += 2
        elif opcode == 5:
            pointer = jump_if_true(instruction)
        elif opcode == 6:
            pointer = jump_if_false(instruction)
        elif opcode == 7:
            pointer += less_than(instruction)
        elif opcode == 8:
            pointer += equals(instruction)
        elif opcode == 9:
            if instruction["p1"] == 0:
                relative_base += instructions[instructions[pointer + 1]]
            elif instruction.get("p1") == 2:
                relative_base += instructions[instructions[pointer + 1] + relative_base]
            else:
                relative_base += instructions[pointer + 1]
            pointer += 2
        else:
            raise Exception("alma")


if __name__ == '__main__':
    instructions = list(input_by_words(","))
    amplify(2)

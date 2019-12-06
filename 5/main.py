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


def parameters(instruction):
    if instruction.get("p1") == 0:
        p1 = instructions[instructions[pointer + 1]]
    else:
        p1 = instructions[pointer + 1]
    if instruction.get("p2") == 0:
        p2 = instructions[instructions[pointer + 2]]
    else:
        p2 = instructions[pointer + 2]
    return p1, p2


def adds(instruction):
    p1, p2 = parameters(instruction)
    instructions[instructions[pointer + 3]] = p1 + p2
    return 4


def multiplies(instruction):
    p1, p2 = parameters(instruction)
    instructions[instructions[pointer + 3]] = p1 * p2
    return 4


def jump_if_true(instruction):
    global pointer
    p1, p2 = parameters(instruction)
    if p1 != 0:
        pointer = p2
        return 0
    else:
        return 3


def jump_if_false(instruction):
    p1, p2 = parameters(instruction)
    return pointer - p2 if p1 == 0 else 3


def less_than(instruction):
    p1, p2 = parameters(instruction)
    instructions[instructions[pointer + 3]] = 1 if p1 < p2 else 0
    return 4


def equals(instruction):
    p1, p2 = parameters(instruction)
    instructions[instructions[pointer + 3]] = 1 if p1 == p2 else 0
    return 4


def write_output():
    output.append(instructions[instructions[pointer + 1]])
    return 2


if __name__ == '__main__':
    instructions = list(input_by_words(","))
    # input = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    input = 5
    output = []
    pointer = 0
    while instructions[pointer] != 99:
        instruction = {
            "opcode": int(str(instructions[pointer])[-1]),
            "p1": 0 if instructions[pointer] < 100 else int(str(instructions[pointer])[-3]),
            "p2": 0 if instructions[pointer] < 1000 else int(str(instructions[pointer])[-4]),
            "p3": 0 if instructions[pointer] < 10000 else int(str(instructions[pointer])[-5])
        }
        opcode = instruction.get("opcode")
        next = 0
        if opcode == 1:
            pointer += adds(instruction)
        elif opcode == 2:
            pointer += multiplies(instruction)
        elif opcode == 3:
            instructions[instructions[pointer + 1]] = input
            pointer += 2
        elif opcode == 4:
            pointer += write_output()
        elif opcode == 5:
            next = jump_if_true(instruction)
            pointer += next
        elif opcode == 6:
            pointer += jump_if_false(instruction)
        elif opcode == 7:
            next = less_than(instruction)
            pointer += next
        elif opcode == 8:
            next = equals(instruction)
            pointer += next

    print(output)



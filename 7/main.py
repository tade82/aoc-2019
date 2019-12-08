import sys
from itertools import permutations
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
        p1 = instructions[instructions[instruction["pointer"] + 1]]
    else:
        p1 = instructions[instruction["pointer"] + 1]
    if instruction.get("p2") == 0:
        p2 = instructions[instructions[instruction["pointer"] + 2]]
    else:
        p2 = instructions[instruction["pointer"] + 2]
    return p1, p2


def adds(instruction):
    p1, p2 = parameters(instruction)
    instructions[instructions[instruction["pointer"] + 3]] = p1 + p2
    return 4


def multiplies(instruction):
    p1, p2 = parameters(instruction)
    instructions[instructions[instruction["pointer"] + 3]] = p1 * p2
    return 4


def jump_if_true(instruction, pointer):
    p1, p2 = parameters(instruction)
    return p2 - pointer if p1 != 0 else 3


def jump_if_false(instruction, pointer):
    p1, p2 = parameters(instruction)
    return p2 - pointer if p1 == 0 else 3


def less_than(instruction):
    p1, p2 = parameters(instruction)
    instructions[instructions[instruction["pointer"] + 3]] = 1 if p1 < p2 else 0
    return 4


def equals(instruction):
    p1, p2 = parameters(instruction)
    instructions[instructions[instruction["pointer"] + 3]] = 1 if p1 == p2 else 0
    return 4


def amplify(input, pointer, memory):
    while memory[pointer] != 99:
        instruction = {
            "pointer": pointer,
            "opcode": memory[pointer] % 100,
            "p1": 0 if memory[pointer] < 100 else int(str(memory[pointer])[-3]),
            "p2": 0 if memory[pointer] < 1000 else int(str(memory[pointer])[-4]),
            "p3": 0 if memory[pointer] < 10000 else int(str(memory[pointer])[-5])
        }
        opcode = instruction.get("opcode")
        if opcode == 1:
            pointer += adds(instruction)
        elif opcode == 2:
            pointer += multiplies(instruction)
        elif opcode == 3:
            memory[memory[pointer + 1]] = input.pop(0)
            pointer += 2
        elif opcode == 4:
            return memory[memory[pointer + 1]], pointer + 2, memory
        elif opcode == 5:
            pointer += jump_if_true(instruction, pointer)
        elif opcode == 6:
            pointer += jump_if_false(instruction, pointer)
        elif opcode == 7:
            pointer += less_than(instruction)
        elif opcode == 8:
            pointer += equals(instruction)
    return 99, 0, []


if __name__ == '__main__':
    instructions = list(input_by_words(","))
    max = 0
    phase_sequence = ()
    for perms in permutations(range(5, 10)):
        memory0 = instructions
        memory1 = instructions
        memory2 = instructions
        memory3 = instructions
        memory4 = instructions
        input0 = [perms[0], 0]
        input1 = [perms[1]]
        input2 = [perms[2]]
        input3 = [perms[3]]
        input4 = [perms[4]]
        p0, p1, p2, p3, p4 = 0, 0, 0, 0, 0
        output4 = 0
        while output4 != 99:
            output0, p0, memory0 = amplify(input0, p0, memory0)
            input1.append(output0)
            output1, p1, memory1 = amplify(input1, p1, memory1)
            input2.append(output1)
            output2, p2, memory2 = amplify(input2, p2, memory2)
            input3.append(output2)
            output3, p3, memory3 = amplify(input3, p3, memory3)
            input4.append(output3)
            output4, p4, memory4 = amplify(input4, p4, memory4)
            input0.append(output4)

            if output4 > max:
                max = output4
                phase_sequence = perms

    print(f"max: {max} {phase_sequence}")

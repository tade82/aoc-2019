import itertools


def read_input():
    with open((__file__.rstrip("main.py") + "input.txt"), "r") as file:
        return file.read()


def input_by_lines():
    return read_input().splitlines()


if __name__ == '__main__':
    input = input_by_lines()[0]
    result = [2 for i in range(150)]
    for i, j in itertools.product(range(100), range(150)):
            index = 150 * (100 - i - 1) + j
            if input[index] == '0':
                result[j] = 0
            if input[index] == '1':
                result[j] = 1

    for j in range(25):
        for b in result[25 * j:25 * j + 25]:
            if b == 1:
                print("o", end=" ")
            else:
                print(" ", end=" ")
        print('')

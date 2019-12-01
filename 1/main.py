from typing import Iterable


def read_input():
    with open((__file__.rstrip("main.py")+"input.txt"), "r") as file:
        return file.read()


def input_by_lines() -> Iterable:
    return read_input().splitlines()


def calculate_fuel(mass) -> int:
    return mass // 3 - 2


def requires_more_fuel(fuel) -> bool:
    return fuel >= 0


if __name__ == '__main__':
    mass_list = input_by_lines()
    sum = 0
    for mass in mass_list:
        required_fuel = calculate_fuel(int(mass))
        while requires_more_fuel(required_fuel):
            sum += required_fuel
            required_fuel = calculate_fuel(required_fuel)

    print(sum)

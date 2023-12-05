from read import read_input
import re

SPELLED_OUT_LETTERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def digit_number_func(numbers):
    numbers = numbers[0], numbers[-1]
    digit_number = int("".join(numbers))
    return digit_number


def part_one(lines):
    final_total = 0

    # Get the fist and last digit from the string
    for line in lines:
        numbers = [char for char in line if char.isdigit()]
        digit_number = digit_number_func(numbers)
        final_total += digit_number

    return final_total


def conver_real_digits(line):
    numbers = []
    digits = re.findall(
        r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))",
        line,
    )
    if digits:
        for digit in digits:
            if digit.isdigit():
                numbers.append(digit)
            else:
                numbers.append(SPELLED_OUT_LETTERS[digit])
    return numbers


def part_two(lines):
    final_total = 0
    for line_o in lines:
        numbers = conver_real_digits(line_o.strip())
        digit_number = digit_number_func(numbers)
        final_total += digit_number

    return final_total


lines = read_input("01")

solution = part_one(lines)
print(f"Day 1; part one: {solution}")

solution = part_two(lines)
print(f"Day 1; part two: {solution}")

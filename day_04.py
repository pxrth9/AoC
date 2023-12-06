from read import read_input

lines = read_input("04")


def get_left_right_numbers(line):
    _, numbers = line.split(":")
    left, right = numbers.split("|")
    left = left.split()
    right = right.split()
    return left, right

def calc_total_points(winners_num):
    total_points = 0
    for i in range(winners_num):
        if i == 0:
            total_points += 1
        else:
            total_points = 2*total_points
    return total_points
        

def part_one(lines):
    total_winners = 0
    for line in lines:
        winners_num = 0
        winners, curr_numbers = get_left_right_numbers(line)
        for number in curr_numbers:
            if number in winners:
                winners_num += 1
        total_points = calc_total_points(winners_num)
        total_winners += total_points
    return total_winners

solution = part_one(lines)
print(f"Day 4; part one: {solution}")


def part_two(lines):
    cards = [1]* len(lines)
    for idx, line in enumerate(lines):
        winners_num = 0
        winners, curr_numbers = get_left_right_numbers(line)
        for number in curr_numbers:
            if number in winners:
                winners_num += 1
        for i in range(winners_num):
            cards[i + 1 + idx] += cards[idx]
    return sum(cards)


solution = part_two(lines)
print(f"Day 4; part two: {solution}")

from read import read_input
import re


def get_game_num(game):
    game_num = re.findall("\d+", game)
    game_num = int(game_num[0])
    return game_num


def get_set_games(subset_cubes):
    subset = subset_cubes.split(";")
    return subset


def get_color_value(color_value):
    val = color_value.strip().split(" ")
    return val[1], int(val[0])


def count_colors(set_games, MAX_VALUES):
    for set_g in set_games:
        round = set_g.split(",")
        for color_value in round:
            color, value = get_color_value(color_value)
            if value > MAX_VALUES[color]:
                return False
    return True


def part_one(lines):
    MAX_VALUES = {"red": 12, "green": 13, "blue": 14}
    final_ans = 0
    for line in lines:
        game, subset_cubes = line.split(":")
        set_games = get_set_games(subset_cubes)
        is_valid = count_colors(set_games, MAX_VALUES)
        if not is_valid:
            continue
        game_num = get_game_num(game)
        final_ans += game_num
    return final_ans


def get_max_color_value_multiplied(set_games):
    MAX_BLUE = MAX_RED = MAX_GREEN = 1
    for set_g in set_games:
        round = set_g.split(",")
        for color_value in round:
            color, value = get_color_value(color_value)
            match color:
                case "blue":
                    MAX_BLUE = max(value, MAX_BLUE)
                case "red":
                    MAX_RED = max(value, MAX_RED)
                case "green":
                    MAX_GREEN = max(value, MAX_GREEN)
    return MAX_GREEN * MAX_BLUE * MAX_RED


def part_two(lines):
    final_ans = 0
    for line in lines:
        _, subset_cubes = line.split(":")
        set_games = get_set_games(subset_cubes)
        multiplied_value = get_max_color_value_multiplied(set_games)
        final_ans += multiplied_value
    return final_ans


lines = read_input("02")

# Part one
solution = part_one(lines)
print(f"Day 2; part one: {solution}")


# Part two
solution = part_two(lines)
print(f"Day 2; part two: {solution}")

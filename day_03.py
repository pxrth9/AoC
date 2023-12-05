from read import read_input

lines = read_input("03_SAMPLE")


def is_valid_matrix(x, y, mat):
    return x < len(mat) and y < len(mat[0])


def part_one(lines):
    print(lines)
    pass


solution = part_one(lines)
print(f"Day ; part one: {solution}")


def part_two(lines):
    pass


solution = part_two(lines)
print(f"Day ; part two: {solution}")

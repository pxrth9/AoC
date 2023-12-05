def read_input(day):
    """Reads the input file for the specified day and returns a list of lines."""
    with open(f"Input/{day}.txt") as f:
        return [line.strip() for line in f.readlines()]

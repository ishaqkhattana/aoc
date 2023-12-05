import re

def calculate_sum(values):
    return sum(values)

def read_file_and_split_lines(file_path):
    """Reads a file and splits the lines into a list of strings.
    """
    with open(file_path, "r") as file:
        input_lines = file.read().splitlines()
    
    return input_lines


def extract_balls_from_game(line):
    """Extracts all balls from a game and returns them as a list of tuples like [(count, color), (count, color), ...].
    """
    all_balls_in_game = re.findall(r'\b(\d+)\s+([a-zA-Z]+)\b', line, flags=re.IGNORECASE)
    if len(all_balls_in_game) == 0:
        Exception("No balls in game!")
        return None
    
    return all_balls_in_game

def read_file_and_split_lines(file_path):
    """Reads a file and splits the lines into a list of strings.
    """
    with open(file_path, "r") as file:
        input_lines = file.read().splitlines()
    
    return input_lines

def calculate_sum(values):
    return sum(values)


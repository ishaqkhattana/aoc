from task_utils import extract_balls_from_game, read_file_and_split_lines

def get_sum_of_powers(input_lines):
    sum_of_powers = 0
    for line in input_lines:
        all_balls_in_game = extract_balls_from_game(line)
        
        if all_balls_in_game:
            color_counts = {'red': 0, 'blue': 0, 'green': 0}
            for count, color in all_balls_in_game:
                count = int(count)
                if count > color_counts[color]:
                    color_counts[color] = count
        
            max_red = color_counts['red']
            max_blue = color_counts['blue']
            max_green = color_counts['green']

            power_of_set = max_red * max_blue * max_green
            sum_of_powers += power_of_set

    return sum_of_powers


if __name__ == "__main__":
    input_lines = read_file_and_split_lines("puzzle_input.txt")
    
    sum_of_powers = get_sum_of_powers(input_lines)

    print(f"Sum of powers: {sum_of_powers}")

    
    
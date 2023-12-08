from task_utils import read_file_and_split_lines, calculate_sum

def is_symbol(char):
    if char != "." and not char.isnumeric():
        return True
    return False

def __adjacent_symbols_helper(line, char_no):
    if is_symbol(line[char_no]):
        return True
    if char_no == 0:
        if is_symbol(line[char_no + 1]):
            return True
    elif char_no == len(line) - 1:
        if is_symbol(line[char_no - 1]):
            return True
    else:
        if is_symbol(line[char_no - 1]) or is_symbol(line[char_no + 1]):
            return True
    return False

def check_adjacent_chars_for_symbols(char_no, line, next_line, previous_line):
    next_line_sideways_symbols = False
    previous_line_sideways_symbols = False
    if next_line:
        next_line_sideways_symbols = __adjacent_symbols_helper(next_line, char_no)

    if previous_line:
        previous_line_sideways_symbols = __adjacent_symbols_helper(previous_line, char_no)

    current_line_sideways_symbols = __adjacent_symbols_helper(line, char_no)

    return next_line_sideways_symbols or previous_line_sideways_symbols or current_line_sideways_symbols

def __adjacent_digits_helper(line, char_no):
    if line[char_no].isnumeric():
        return True
    if char_no == 0:
        if line[char_no + 1].isnumeric():
            return True
    elif char_no == len(line) - 1:
        if line[char_no - 1].isnumeric():
            return True
    else:
        if is_symbol(line[char_no - 1]) or is_symbol(line[char_no + 1]):
            return True
    return False

def get_gear_ratios(modified_engine_schematic):
    gear_ratios = []
    for row_no, row in enumerate(modified_engine_schematic):
        for char_no, char in enumerate(row):
            if char == "*":
                # Find part numbers in adjacent or diagonal cells
                temp_gears = set()
                if row_no > 0 and row_no < len(modified_engine_schematic) - 1:
                    if char_no > 0 and char_no < len(row) - 1:
                        if type(modified_engine_schematic[row_no - 1][char_no - 1]) == dict:
                            temp_gears.add(modified_engine_schematic[row_no - 1][char_no - 1]["number"])
                        if type(modified_engine_schematic[row_no - 1][char_no]) == dict:
                            temp_gears.add(modified_engine_schematic[row_no - 1][char_no]["number"])
                        if type(modified_engine_schematic[row_no - 1][char_no + 1]) == dict:
                            temp_gears.add(modified_engine_schematic[row_no - 1][char_no + 1]["number"])
                        if type(modified_engine_schematic[row_no][char_no - 1]) == dict:
                            temp_gears.add(modified_engine_schematic[row_no][char_no - 1]["number"])
                        if type(modified_engine_schematic[row_no][char_no + 1]) == dict:
                            temp_gears.add(modified_engine_schematic[row_no][char_no + 1]["number"])
                        if type(modified_engine_schematic[row_no + 1][char_no - 1]) == dict:
                            temp_gears.add(modified_engine_schematic[row_no + 1][char_no - 1]["number"])
                        if type(modified_engine_schematic[row_no + 1][char_no]) == dict:
                            temp_gears.add(modified_engine_schematic[row_no + 1][char_no]["number"])
                        if type(modified_engine_schematic[row_no + 1][char_no + 1]) == dict:
                            temp_gears.add(modified_engine_schematic[row_no + 1][char_no + 1]["number"])
                        
                        if len(temp_gears) == 2:
                            mul = 1
                            for number in temp_gears:
                                mul *= number
                            gear_ratios.append(mul)
    return gear_ratios

def get_sum_of_gear_ratios(lines):
    modified_engine_schematic = [['.' for _ in range(len(line))] for line in lines] # Populate a 2D array replicating the input

    for line_no, line in enumerate(lines):
        for char_no, char in enumerate(line):
            modified_engine_schematic[line_no][char_no] = '.'  # Add in all the *'s here as the loop below skips iterations
            if char == "*":
                modified_engine_schematic[line_no][char_no] = "*"

    for line_no, line in enumerate(lines):
        previous_line = None
        next_line = None
        if not line_no == 0:
            previous_line = lines[line_no - 1]
        if not line_no == len(lines) - 1:
            next_line = lines[line_no + 1]

        char_iterator = iter(line)
        temp_number = {
            "number": "",
            "indices": []
        }
        char_index = 0

        for char in char_iterator:
            if char.isnumeric():
                temp_index = char_index
                temp_counter = 0

                while line[temp_index].isnumeric():
                    temp_number["number"] += line[temp_index]
                    temp_number["indices"] += [temp_index]
                    temp_index += 1
                    temp_counter += 1
                    if temp_index == len(line):
                        break

                for index in temp_number["indices"]:
                    if check_adjacent_chars_for_symbols(index, line, next_line, previous_line):
                        digit_counter = 0
                        for index in temp_number["indices"]:
                            modified_engine_schematic[line_no][index] = {"digit": temp_number["number"][digit_counter], "number": int(temp_number["number"])}
                            digit_counter += 1
                        break

                temp_number["number"] = ""
                temp_number["indices"] = []

                for _ in range(temp_counter):
                    try:
                        char_index += 1
                        next(char_iterator)
                    except StopIteration:
                        break

            char_index += 1
    gears = get_gear_ratios(modified_engine_schematic)
    return calculate_sum(gears)

if __name__ == "__main__":
    input_lines = read_file_and_split_lines("puzzle_input.txt")
    sum_of_gear_ratios = get_sum_of_gear_ratios(input_lines)
    print(f"sum of gear ratios: {sum_of_gear_ratios}")
    exit(0)
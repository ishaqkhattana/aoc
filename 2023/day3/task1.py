from task_utils import read_file_and_split_lines, calculate_sum

def is_symbol(char):
    if char != "." and not char.isnumeric():
        return True
    return False

def __adjacent_symbols_helper(line, char_no):
    if is_symbol(line[char_no]): # Is the char itself a symbol? Valid for cases where this function is called for next and prev lines
        return True
    if char_no == 0:
        if is_symbol(line[char_no +1]):
            return True
    elif char_no == len(line) -1:
        if is_symbol(line[char_no -1]):
            return True
    else:
        if is_symbol(line[char_no -1]) or is_symbol(line[char_no +1]):
            return True
    return False

def check_adjacent_chars_for_symbols(char_no, line, next_line, previous_line):
    next_line_sideways_symbols = False
    previous_line_sideways_symbols = False
    if next_line:
        next_line_sideways_symbols =  __adjacent_symbols_helper(next_line, char_no)
        
    if previous_line:
        previous_line_sideways_symbols =  __adjacent_symbols_helper(previous_line, char_no)
    
    current_line_sideways_symbols =  __adjacent_symbols_helper(line, char_no)

    return next_line_sideways_symbols or previous_line_sideways_symbols or current_line_sideways_symbols
    

def get_part_numbers(lines):
    part_numbers = []
    for line_no, line in enumerate(lines):
        previous_line = None
        next_line = None
        if not line_no == 0:
            previous_line = lines[line_no -1]
        if not line_no == len(lines) -1:
            next_line = lines[line_no +1]
        
        char_iterator = iter(line)
        temp_number = {
            "number": "",
            "indices": []
        }
        char_index = 0
        for char in char_iterator:
            # Don't be scared of all the loops in here, they all run a maximum of 3 times given the input constraints and are O(1)
            if char.isnumeric() and char != "":
                # as we encounter a digit, we construct the entire number alongwith its char indices
                temp_index = char_index
                temp_counter = 0  ## Keeps track of how many digits to skip in the enclosing for loop incase a part number is found
                while line[temp_index].isnumeric():
                    temp_number["number"] += line[temp_index]
                    temp_number["indices"] += [temp_index]
                    temp_index += 1
                    temp_counter += 1
                    if temp_index == len(line):
                        break
                
                # Check if any of the indices in the temp_number have adjacent symbols
                for index in temp_number["indices"]:
                    if check_adjacent_chars_for_symbols(index, line, next_line, previous_line):
                        part_numbers.append(int(temp_number["number"]))
                        break  # Break out of the loop to avoid duplicate matches within the same number
                    
                # Skip the for loop by number of digits we just found in the number and clear temp_number
                temp_number["number"] = ""
                temp_number["indices"] = []
                for _ in range(temp_counter):
                    try:
                        char_index +=1
                        next(char_iterator)
                    except StopIteration:
                        break
            char_index += 1

    print(part_numbers)
    return part_numbers


if __name__ == "__main__":
    input_lines = read_file_and_split_lines("puzzle_input.txt")
    part_numbers = get_part_numbers(input_lines)
    sum_of_part_numbers = calculate_sum(part_numbers)
    print(f"sum of part numbers: {sum_of_part_numbers}")
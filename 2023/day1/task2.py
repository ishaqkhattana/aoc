import re

def extract_calibration_values(lines):
    values = []
    for line in lines:
        # Find all digits or digit words in the line
        digit_matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line, flags=re.IGNORECASE)
        
        # Extract the first and last digit or digit word
        first_digit = digit_matches[0] if digit_matches else ''
        last_digit = digit_matches[-1] if digit_matches else ''
        
        # Convert digit words to corresponding digits
        if first_digit.isalpha():
            first_digit = convert_digit_word_to_digit(first_digit)
        if last_digit.isalpha():
            last_digit = convert_digit_word_to_digit(last_digit)
        
        # Add the calibration value to the list
        if first_digit and last_digit:
            calibration_value = int(str(first_digit) + str(last_digit))
            values.append(calibration_value)
    
    return values

def convert_digit_word_to_digit(word):
    digit_words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return digit_words.get(word.lower(), 0)

def calculate_sum(calibration_values):
    return sum(calibration_values)

if __name__ == "__main__":
    input_file_path = "puzzle_input.txt"
    
    with open(input_file_path, "r") as file:
        input_lines = file.read().splitlines()

    calibration_values = extract_calibration_values(input_lines)
    total_sum = calculate_sum(calibration_values)

    print(f"Calibration values: {calibration_values}")
    print(f"Total sum: {total_sum}")

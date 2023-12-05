def extract_calibration_values(lines):
    values = []
    for line in lines:
        first_digit = next((char for char in line if char.isdigit()), '')
        last_digit = next((char for char in reversed(line) if char.isdigit()), '')
        
        if first_digit and last_digit:
            calibration_value = int(first_digit + last_digit)
            values.append(calibration_value)
    
    return values

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

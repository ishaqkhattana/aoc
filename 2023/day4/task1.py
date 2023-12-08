from task_utils import read_file_and_split_lines

def solve(lines):
    sum_of_all_cards = 0

    for line_no, line in enumerate(lines):
        winning_numbers = set()
        card_sum = 0
        delimiter_position = 0
        temp_number = ""

        # Get all the winning numbers until | is found
        for char_no, char in enumerate(line):
            if char == "|":
                delimiter_position = char_no
                break
            elif char.isnumeric():
                temp_number += char
            elif char == " " and temp_number != "":
                winning_numbers.add(int(temp_number))
                temp_number = ""

        # Now we have all the winning numbers, we check if our card is in the set,
        # if it is, we pop it and sum the card
        temp_number = ""
        for i in range(delimiter_position + 1, len(line) + 1):  # Include the end to process the last number
            if i == len(line) or line[i].isspace():
                if temp_number:
                    if int(temp_number) in winning_numbers:
                        if card_sum == 0:
                            card_sum = 1
                        else:
                            card_sum *= 2
                    temp_number = ""
            elif line[i].isnumeric():
                temp_number += line[i]

        sum_of_all_cards += card_sum
    print("sum of all cards is {}".format(sum_of_all_cards))

if __name__ == "__main__":
    input_lines = read_file_and_split_lines("puzzle_input.txt")
    # Remove part of the input line until :
    for line_no, line in enumerate(input_lines):
        input_lines[line_no] = line.split(":")[1].strip()
    solve(input_lines)

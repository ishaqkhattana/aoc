from task_utils import calculate_sum, extract_balls_from_game, read_file_and_split_lines

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def get_valid_games(input_lines):
    game_id = 1
    valid_games = []
    for line in input_lines:
        invalid = False
        all_balls_in_game = extract_balls_from_game(line)
        
        if all_balls_in_game:
            for ball in all_balls_in_game:
                if len(ball) != 2:
                    Exception("Ball is invalid in game: {game_id}!}")

                red_count = 0
                blue_count = 0
                green_count = 0
                if ball[1].lower() == "red":
                    red_count += int(ball[0])
                elif ball[1].lower() == "blue":
                    blue_count += int(ball[0])
                elif ball[1].lower() == "green":
                    green_count += int(ball[0])
                
                if red_count > RED_MAX or blue_count > BLUE_MAX or green_count > GREEN_MAX:
                    print(f"Game {game_id} is invalid!")
                    invalid = True
                    break
        if invalid:
            invalid = False
            game_id+=1
            continue
        print(f"Game {game_id} is valid!")
        valid_games.append(game_id)
        game_id+=1

    return valid_games


if __name__ == "__main__":
    input_lines = read_file_and_split_lines("puzzle_input.txt")
    
    valid_games = get_valid_games(input_lines)

    sum_of_valid_games = calculate_sum(valid_games)

    print(f"Valid games: {valid_games}")
    print(f"Sum of valid games: {sum_of_valid_games}")

    
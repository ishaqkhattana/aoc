def convert_number(source, destination_map):
    for dest_start, source_start, length in destination_map:
        if source_start <= source < source_start + length:
            return dest_start + (source - source_start)
    return source

def find_lowest_location(seed, almanac):
    current_number = seed
    for category_map in almanac:
        current_number = convert_number(current_number, category_map)
    return current_number

def read_input_from_file(file_path):
    seeds = []
    almanac = []

    with open(file_path, 'r') as file:
        current_section = None
        for line in file:
            line = line.strip()
            if line.startswith("seeds:"):
                seeds = list(map(int, line.split()[1:]))
            elif line.endswith("map:"):
                if current_section is not None:
                    almanac.append(current_section)
                current_section = []
            elif line and current_section is not None:
                values = list(map(int, line.split()))
                current_section.append((values[0], values[1], values[2]))

        if current_section is not None:
            almanac.append(current_section)

    return seeds, almanac

def main():
    file_path = "puzzle_input.txt"
    seeds, almanac = read_input_from_file(file_path)
    print("almanac:", almanac)
    lowest_location = float('inf')
    
    for seed in seeds:
        print("seed:", seed)
        location = find_lowest_location(seed, almanac) 
        print("location:", location)
        lowest_location = min(lowest_location, location)

    print("Lowest Location Number:", lowest_location)

if __name__ == "__main__":
    main()

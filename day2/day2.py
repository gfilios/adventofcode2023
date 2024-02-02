import re

game_id_regex = re.compile('^Game (\d+):')
blue_regex = re.compile('.*(\d+) blue')
green_regex = re.compile('.*(\d+) green')
red_regex = re.compile('.*(\d+) red')

'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

#only 12 red cubes, 13 green cubes, and 14 blue cubes?
'''
valid_red = 12
valid_blue = 14
valid_green = 13


def balls_in_set(set):
    red = 0
    blue = 0
    green = 0
    elements = set.split(",")
    for element in elements:
        parts = element.strip().split(" ")
        color = parts[1].strip()
        if color == "red":
            red = int(parts[0])
        elif color == "green":
            green = int(parts[0])
        elif color == "blue":
            blue = int(parts[0])
    return red, blue, green


def are_balls_valid(red, green, blue):
    return (red <= valid_red) and (green <= valid_green) and (blue <= valid_blue)


def validate_game(game):
    game_id = game_id_regex.match(game).group(1)
    sets = game[6 + len(game_id):].split(';')
    return_value = int(game_id)
    for set in sets:
        (red, blue, green) = balls_in_set(set)
        if not (are_balls_valid(red, green, blue)):
            return_value = 0
    return return_value


def minimum_cubes(line):
    min_red = 0
    min_green = 0
    min_blue = 0

    game_id = game_id_regex.match(line).group(1)
    sets = line[6 + len(game_id):].split(';')
    for set in sets:
        (red, blue, green) = balls_in_set(set)
        min_red = max(min_red, red)
        min_blue = max(min_blue, blue)
        min_green = max(min_green, green)
    return min_red * min_blue * min_green


def validate_games(games):
    sum = 0
    with open(games) as f:
        game = f.readline().strip('\n')
        while game:
            value = validate_game(game)
            sum = sum + value
            game = f.readline().strip('\n')
    return sum


def min_cubes_needed(file):
    sum = 0
    with open(file) as f:
        line = f.readline().strip('\n')
        while line:
            value = minimum_cubes(line)
            sum = sum + value
            line = f.readline().strip('\n')
    return sum


print(f"Day 2, Part 1 = {validate_games('input.txt.txt')}")
print(f"Day 2, Part 2 = {min_cubes_needed('input.txt')}")

'''
seed-to-soil map:
soil-to-fertilizer map:
fertilizer-to-water map:
water-to-light map:
light-to-temperature map:
temperature-to-humidity map:
humidity-to-location map:
'''
import re

section_regex = re.compile('^(.*) map:')

mappings = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': [],
}

seeds = []


def reset_mapping():
    for section in mappings.keys():
        mappings[section] = []


def read_mappings():
    global mappings
    global seeds
    reset_mapping()
    #almanac = open('input_debug.txt').read().splitlines()
    almanac = open('input.txt').read().splitlines()
    seeds = [eval(i) for i in (almanac[0].split(":")[1].strip().split(" "))]
    current_mapping = []
    for line in almanac[1:]:
        section_match = section_regex.match(line)
        if section_match is not None:
            section = section_match.group(1)
            current_mapping = mappings[section]
        else:
            if line != "":
                current_mapping.append([eval(i) for i in (line.strip().split(" "))])
    sort_mapping()

def map_value_to_section(value, section):
    global mappings
    mapped_value = -1
    for map in mappings[section]:
        if value >= map[1] and value < (map[1] + map[2]):
            mapped_value = map[0] + (value - map[1])
    if mapped_value == -1:
        mapped_value = value

    return mapped_value


def local_min(a, b):
    if a == -1:
        return b
    return min(a, b)


def map_seeds_part1():
    read_mappings()
    lowest = -1
    for seed in seeds:
        next_value = seed
        for section in mappings.keys():
            next_value = map_value_to_section(next_value, section)
        lowest = local_min(lowest, next_value)
    return lowest


def map_seeds_part2_brute_force():
    read_mappings()
    lowest = -1
    seed_iteration = iter(seeds)
    for seed in seed_iteration:
        next_value = seed
        next_range = next(seed_iteration)
        print(f"Seed {next_value} and Range {next_range}")
        for seedValue in range(next_value, next_value + next_range):

            mapped_result = seedValue
            for section in mappings.keys():
                mapped_result = map_value_to_section(mapped_result, section)
            lowest = local_min(lowest, mapped_result)
    return lowest


def sort_mapping():
    for section in mappings.keys():
        mappings[section] = sorted(mappings[section], key=lambda item: item[1])





if __name__ == '__main__':
    print(f"Part 1: {map_seeds_part1()}")
    print(f"Part 2: {map_seeds_part2_brute_force()}")

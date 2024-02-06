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


def read_mappings():
    global mappings
    global seeds
    almanac = open('input_debug.txt').read().splitlines()
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


def map_seeds(part=1):
    read_mappings()
    lowest = -1
    seed_iteration = iter(seeds)
    for seed in seed_iteration:
        next_value = seed
        if part == 2:
            next(seed_iteration)
        print(next_value)
        for section in mappings.keys():
            next_value = map_value_to_section(next_value, section)
        lowest = local_min(lowest, next_value)
    return lowest


if __name__ == '__main__':
    print(f"Part 1: {map_seeds()}")
    print(f"Part 2: {map_seeds(2)}")

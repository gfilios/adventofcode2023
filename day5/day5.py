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
from time import sleep
from threading import Thread, current_thread

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
def sort_mapping():
    for section in mappings.keys():
        mappings[section] = sorted(mappings[section], key=lambda item: item[1])

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
    global mappings
    min_values = []
    read_mappings()
    threads = []
    lowest = -1
    seed_iteration = iter(seeds)
    for seed in seed_iteration:
        next_value = seed
        next_range = next(seed_iteration)
        print()
        thread = Thread(target=map_seed_range, args=(next_value, next_range, mappings, min_values ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return min(min_values)


def map_seed_range(seed_start, seed_range, mappings, min_values):
    lowest = -1
    thread = current_thread()
    print(f"{thread.name}: From {seed_start} and Range {seed_range}")
    for seedValue in range(seed_start, seed_start + seed_range):
        mapped_result = seedValue
        for section in mappings.keys():
            mapped_result = map_value_to_section(mapped_result, section)
        lowest = local_min(lowest, mapped_result)
    print(f"{thread.name}: Result {lowest}")
    min_values.append(lowest)


if __name__ == '__main__':
    print(f"Part 1: {map_seeds_part1()}")
    print(f"Part 2: {map_seeds_part2_brute_force()}")

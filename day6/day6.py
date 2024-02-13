import math


def sqrtvalue(time, distance_to_beat):
    return math.sqrt(time * time - 4 * distance_to_beat)


def min_wait_time(time, distance_to_beat):
    float_wait_time = (time - sqrtvalue(time, distance_to_beat)) / 2
    wait_time = math.ceil(float_wait_time)
    if wait_time == float_wait_time:
        wait_time = wait_time + 1
    return wait_time


def max_wait_time(time, distance_to_beat):
    float_wait_time = (time + sqrtvalue(time, distance_to_beat)) / 2
    wait_time = math.floor(float_wait_time)
    if wait_time == float_wait_time:
        wait_time = wait_time - 1
    return wait_time


def calc_race(data):
    result = 1
    for race in data:
        min_time = min_wait_time(race[0], race[1])
        max_time = max_wait_time(race[0], race[1])
        # print(f" {race} => {mintime}, {maxtime} = {maxtime - mintime + 1}")
        if result == 1:
            result = (max_time - min_time + 1)
        else:
            result = result * (max_time - min_time + 1)
    return result


if __name__ == '__main__':
    # time, distance
    testdata = [(7, 9), (15, 40), (30, 200)]
    realdata = [(47, 400), (98, 1213), (66, 1011), (98, 1540)]

    print(f"Day 6, Part 1: The answer for {testdata}is: {calc_race(testdata)}")
    print(f"Day 6, Part 1: The answer for {realdata}is: {calc_race(realdata)}")

    testdata = [(71530, 940200)]
    realdata = [(47986698, 400121310111540)]
    print(f"Day 6, Part 2: The answer for {testdata}is: {calc_race(testdata)}")
    print(f"Day 6, Part 2: The answer for {realdata}is: {calc_race(realdata)}")
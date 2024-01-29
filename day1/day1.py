import re
import sys

# firstDigit = re.compile('^[a-zA-Z]*(\d|one|two|three|four|five|six|seven|eight|nine|zero]{1})[a-zA-Z0-9]*')
# lastDigit = re.compile('^[a-zA-Z0-9]*(\d|one|two|three|four|five|six|seven|eight|nine|zero{1})[a-zA-Z]*')

digit = re.compile('\d')
digitandnumbers = re.compile('\d|one|two|three|four|five|six|seven|eight|nine')
overlapps = re.compile('oneight|threeight|fiveight|nineight|twone|sevenine|eightwo')

lookup = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9",
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'oneight': "8",
    'threeight': "8",
    'fiveight': "8",
    'nineight': "8",
    'twone': "1",
    'sevenine': "9",
    'eightwo' : "2"
}


def digits_only(line):
    results = digit.findall(line)
    return int(results[0] + results[-1])


def digits_and_numbers(line):
    left = lookup[digitandnumbers.findall(line)[0]]
    right = get_right(line)
    result = left + right
    return int(result)


def get_right(line):
    right_value = ""
    right_pos = -1
    for m in digitandnumbers.finditer(line):
        right_value = m.group()
        right_pos = m.start()

    for m in overlapps.finditer(line):
        if m.start() == right_pos:
            right_value = m.group()
    right = lookup[right_value]
    return right


def calc_sum(file, sumfunction):
    sum = 0
    with open(file) as f:
        line = f.readline().strip('\n')
        while line:
            value = sumfunction(line)
            sum = sum + value
            line = f.readline().strip('\n')
    return sum


print(f"Day 1, Part 1 = {calc_sum('input.txt', digits_only)}")
print(f"Day 1, Part 2 = {calc_sum('input.txt', digits_and_numbers)}")

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


def digits_and_numbers_over(line):
    left = lookup[digitandnumbers.findall(line)[0]]
    right = get_right(line)
    right2 = get_right_alt(line)
    if (right2 != right):
        print(line, right, right2)
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


def get_right_alt(line):
    right_value = None
    startsearch = len(line)
    while right_value is None:
        right_value = digitandnumbers.search(line, startsearch)
        startsearch = startsearch - 1

    right = lookup[right_value.group()]
    return right


def digits_and_numbers(line):
    results = digitandnumbers.findall(line)
    left = lookup[results[0]]
    right = lookup[results[-1]]
    result = left + right
    return int(result)


def calc_sum(file, sumfunction):
    sum = 0
    with open(file) as f:
        line = f.readline().strip('\n')
        while line:
            value = sumfunction(line)
            sum = sum + value
            line = f.readline().strip('\n')
    return sum


print("zsgdgdgdgoneight", digits_and_numbers_over("zsgdgdgdgoneight"))
print(calc_sum('input.txt', digits_only))
print(calc_sum('input.txt', digits_and_numbers))
print(calc_sum('input.txt', digits_and_numbers_over))

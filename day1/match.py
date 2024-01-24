import re
import sys

firstDigit = re.compile('^[a-zA-Z]*([0-9]{1})[a-zA-Z0-9]*')
lastDigit = re.compile('^[a-zA-Z0-9]*([0-9]{1})[a-zA-Z]*')


def regex_search(line):
    first_match = firstDigit.match(line).group(1)
    second_match = lastDigit.match(line).group(1)
    return int(first_match + second_match)

sum = 0
sum_d = 0
with open('input.txt') as f:
    line = f.readline()
    while line:
        lineclean = line.strip('\n')
        value = regex_search(line)
        sum = sum + value

        line = f.readline()

print(sum)

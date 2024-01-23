import re
import sys

firstDigit = re.compile('^[a-zA-Z]*([0-9]{1})[a-zA-Z0-9]*')
lastDigit = re.compile('^[a-zA-Z0-9]*([0-9]{1})[a-zA-Z]*')

sum = 0
with open('input.txt') as f:
    line=f.readline()
    while line:
      lineclean = line.strip('\n')
      firstMatch = firstDigit.match(lineclean)
      secondMatch = lastDigit.match(lineclean)
      print(f'{lineclean}, {firstMatch.group(1)}, {secondMatch.group(1)}')
      line=f.readline()
      sum = sum + int(firstMatch.group(1)) + int(secondMatch.group(1))

print(sum)
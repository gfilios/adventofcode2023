import re
import sys

p = re.compile('^[a-zA-Z]*([0-9])+')


with open('input.txt') as f:
    line=f.readline()
    while line:
      lineclean = line.strip('\n')
      m = p.match(lineclean)
      print(f'{lineclean}, {m.group(1 )}')
      line=f.readline()

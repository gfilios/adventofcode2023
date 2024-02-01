import re
from collections import defaultdict

number_regex = re.compile('\d+')
dots_regex = re.compile('\.')
digit_regex = re.compile('\d')
gear_regex = re.compile('\*')

plan = open('input.txt').read().splitlines()
line_count = len(plan)
line_len = len(plan[0])


def valid_part(match, plan, lno):
    from_col, from_line, to_col, to_line = corona(lno, match)

    max_dots_or_digits = to_col - from_col
    for line in range(from_line, to_line + 1):
        line_part = plan[line][from_col:to_col]
        dots = len(dots_regex.findall(line_part))
        digits = len(digit_regex.findall(line_part))
        if (dots + digits) < max_dots_or_digits:
            # print(f"Match {lno}: {match.group()}")
            return int(match.group())

    return 0


def identify_numbers(plan):
    lno = 0
    sum = 0
    for line in plan:
        for match in number_regex.finditer(line):
            sum += valid_part(match, plan, lno)
        lno += 1
    return sum


def valid_gear(match, plan, lno, stars):
    from_col, from_line, to_col, to_line = corona(lno, match)

    number_chars = to_col - from_col
    for line in range(from_line, to_line + 1):
        line_part = plan[line][from_col:to_col]
        for star in gear_regex.finditer(line_part):
            col = star.start() + from_col
            if (line, col) in stars:
                stars[(line, col)].append(int(match.group()))
            else:
                stars[(line, col)] = [int(match.group())]
    return 0


def corona(lno, match):
    from_col = max(0, match.span()[0] - 1)
    to_col = min(match.span()[1] + 1, line_len)
    from_line = max(0, lno - 1)
    to_line = min(line_count - 1, lno + 1)
    return from_col, from_line, to_col, to_line


def identify_gear(plan):
    lno = 0
    sum = 0
    stars = defaultdict()
    for line in plan:
        for match in number_regex.finditer(line):
            sum += valid_gear(match, plan, lno, stars)
        lno += 1
    for gears in stars.values():
        if len(gears) == 2:
            sum = sum + (gears[0] * gears[1])
    return sum


if __name__ == '__main__':
    print(f" Day 3 - Part 1: Result = {identify_numbers(plan)}")
    print(f" Day 3 - Part 2: Result = {identify_gear(plan)}")

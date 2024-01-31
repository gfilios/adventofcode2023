import re

number_regex = re.compile('\d+')
dots_regex = re.compile('\.')
digit_regex = re.compile('\d')

plan = open('input.txt').read().splitlines()
line_count = len(plan)
line_len = len(plan[0])


def valid_part(match, plan, lno):
    from_col = max(0, match.span()[0] - 1)
    to_col = min(match.span()[1] + 1, line_len)
    from_line = max(0, lno - 1)
    to_line = min(line_count-1, lno + 1)

    number_chars = to_col-from_col
    for line in range(from_line, to_line+1):
        line_part = plan[line][from_col:to_col]
        dots = len(dots_regex.findall(line_part))
        digits = len(digit_regex.findall(line_part))
        if (dots+digits)<number_chars:
            #print(f"Match {lno}: {match.group()}")
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


if __name__ == '__main__':
    print(identify_numbers(plan))

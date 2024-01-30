import re

number_regex = re.compile('\d+')


def valid_part(match, plan, lno):
    span = match.span()
    span0 = match.span()[0] - 1
    span1 = match.span()[1] + 1
    if span0 < 0:
        span0 = 0
    if span1 > len(plan[lno]):
        span1 = len(plan[lno])

    corona = ""
    if (lno > 0):
        corona = corona + plan[lno - 1][span0:span1]
    corona = corona + plan[lno][span0]
    if (lno < len(plan)):
        corona = corona + plan[lno + 1][span0:span1]


def identify_numbers(plan):
    lno = 0
    sum = 0
    for line in plan:
        matches = number_regex.findall(line)
        for match in matches:
            sum += valid_part(match, plan, lno)
        lno += 1
    return sum


if __name__ == '__main__':
    f = open('input.txt', 'r')
    plan = f.readlines()
    identify_numbers(plan)

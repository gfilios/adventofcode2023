import re
card_id_regex = re.compile('(\d+):')

cards = open('input.txt').read().splitlines()


def winning_point():
    sum = 0
    for card in cards:
        card_id = card_id_regex.search(card).group(1)
        numbers = card.strip().split(":")[1].split("|")
        winning_number_list = re.sub(r'\s+', ',', numbers[0].strip()).split(',')
        winning_numbers = set(winning_number_list)
        scratched_number_list = re.sub(r'\s+', ',', numbers[1].strip()).split(',')
        scratched_numbers = set(scratched_number_list)
        hit = 0
        for number in scratched_numbers:
            if number in winning_numbers:
                hit = hit +1
        if (hit > 0):
            sum = sum + (1<<(hit-1))

    return sum

if __name__ == '__main__':
    print(f"Day 4 - part 1: {winning_point()}")
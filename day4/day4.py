import re
card_id_regex = re.compile('(\d+):')

cards = open('input.txt').read().splitlines()


def winning_point():
    sum = 0
    for card in cards:
        card_id = card_id_regex.search(card).group(1)
        hits = get_hits(card)
        if (hits > 0):
            sum = sum + (1<<(hits-1))

    return sum


def get_hits(card):
    numbers = card.strip().split(":")[1].split("|")
    winning_number_list = re.sub(r'\s+', ',', numbers[0].strip()).split(',')
    winning_numbers = set(winning_number_list)
    scratched_number_list = re.sub(r'\s+', ',', numbers[1].strip()).split(',')
    scratched_numbers = set(scratched_number_list)
    hit = 0
    for number in scratched_numbers:
        if number in winning_numbers:
            hit = hit + 1
    return hit


def copies_of_winning_point():
    cards_in_stack = len(cards)
    hits_in_card = []
    card_copies = []

    for card in cards:
        hits = get_hits(card)
        hits_in_card.append(hits)
        card_copies.append(1)

    for idx in range(cards_in_stack):
        hits = hits_in_card[idx]
        for copy_idx in range(idx+1, min(idx+1+hits,cards_in_stack )):
            card_copies[copy_idx] = card_copies[copy_idx]+card_copies[idx]

    sum = 0
    for copies in card_copies:
        sum = sum + copies

    return sum

if __name__ == '__main__':
    print(f"Day 4 - part 1: {winning_point()}")
    print(f"Day 4 - part 2: {copies_of_winning_point()}")
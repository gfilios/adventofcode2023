from operator import itemgetter, attrgetter
from functools import cmp_to_key

symbol_to_hex = [["A", "F"], ["K", "D"], ["Q", "C"], ["J", "B"], ["T", "A"]]


def read_cards_part1(filename: str):
    game_deck = []
    with open(filename) as f:
        line = f.readline().strip('\n')
        while line:
            values = line.split(" ")
            game_deck.append([values[0], int(values[1]), first_order(values[0]), second_order(values)])
            line = f.readline().strip('\n')
    return game_deck


def second_order(card):
    return int(card_to_hex(card[0]), 16)


def card_to_hex(card_value):
    hex_representation = card_value
    for replacement in symbol_to_hex:
        hex_representation = hex_representation.replace(replacement[0], replacement[1])
    hex_representation = "0x" + hex_representation
    return hex_representation


def first_order(card):
    if is_five_of_a_kind(card):
        return 6
    elif is_x_of_a_kind(card, 4):
        return 5
    elif is_full_house(card):
        return 4
    elif is_x_of_a_kind(card, 3):
        return 3
    elif is_two_pair(card):
        return 2
    elif is_x_of_a_kind(card, 2):
        return 1
    return 0


def is_x_of_a_kind(card, x):
    card_value = card
    counter = count_cards(card_value)
    for values in counter.values():
        if (values == x):
            return True

    return False

def is_five_of_a_kind(card):
    card_value = card
    counter = count_cards(card_value)
    condition_full_house = False
    for values in counter.values():
        if (values == 5):
            condition_full_house =  True

    return condition_full_house


def cmp_simple_card(card1, card2):
    result = cmp_values(card1[1], card2[1])
    return result


def cmp_card(card1, card2):
    result = cmp_values(card1[2], card2[2])
    if result == 0:
        result = cmp_values(card1[3], card2[3])

    return result


def cmp_values(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    return -1


def is_full_house(card):
    card_value = card
    counter = count_cards(card_value)

    is_full_house_condition = False
    if len(counter.keys()) == 2:
        cards = list(counter.values())
        is_full_house_condition = (cards[0] == 2 and cards[1] == 3) or (cards[0] == 3 and cards[1] == 2)

    return is_full_house_condition


def is_two_pair(card):
    card_value = card
    counter = count_cards(card_value)

    is_two_pair_condition = False
    if len(counter.keys()) == 3:
        cards = list(counter.values())
        is_two_pair_condition = (cards[0] == 2 and cards[1] == 2) or (cards[0] == 2 and cards[2] == 2) or (
                    cards[1] == 2 and cards[2] == 2)

    return is_two_pair_condition


def count_cards(card_value):
    counter = {}
    for next_card in card_value:
        if counter.get(next_card) is None:
            counter[next_card] = 1
        else:
            counter[next_card] += 1
    return counter

def evaluate_deck(deck):
    sorted_deck = sorted(deck, key=cmp_to_key(cmp_card))
    result = 0
    for rank, card in enumerate(sorted_deck):
        result = result + (rank + 1) * card[1]
    return result

if __name__ == '__main__':
    demo_file = "demo.txt"
    puzzle_file = "input.txt"
    file = demo_file
    file = puzzle_file
    part1_deck = read_cards_part1(file)
    print(f"Day 7, Part 2: {evaluate_deck(part1_deck)}")
#    test_card()

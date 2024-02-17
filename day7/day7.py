from operator import itemgetter, attrgetter
from functools import cmp_to_key

symbol_to_hex = [["A", "F"], ["K", "E"], ["Q", "D"], ["J", "C"], ["T", "B"]]


def read_cards_part1(filename: str, with_joker=False):
    game_deck = []
    with open(filename) as f:
        line = f.readline().strip('\n')
        while line:
            values = line.split(" ")
            bid = int(values[1])
            first_sort = first_order(values[0], with_joker)
            hex = card_to_hex(values[0], with_joker)
            second_sort = int(hex, 16)
            card_codes = [values[0], bid, first_sort, second_sort, hex]
            game_deck.append(card_codes)
            line = f.readline().strip('\n')
    return game_deck


def second_order(card, with_joker=False):
    return int(card_to_hex(card[0], with_joker), 16)


def card_to_hex(card_value, with_joker=False):
    hex_representation = card_value
    if with_joker:
        hex_representation = hex_representation.replace("J", "1")

    for replacement in symbol_to_hex:
        hex_representation = hex_representation.replace(replacement[0], replacement[1])

    hex_representation = "0x" + hex_representation
    return hex_representation


def first_order(card, with_joker=False):
    if is_five_of_a_kind(card, with_joker):
        return 6
    elif is_x_of_a_kind(card, 4, with_joker):
        return 5
    elif is_full_house(card, with_joker):
        return 4
    elif is_x_of_a_kind(card, 3, with_joker):
        return 3
    elif is_two_pair(card, with_joker):
        return 2
    elif is_x_of_a_kind(card, 2, with_joker):
        return 1
    return 0


def number_of_joker(counter):
    if "J" in counter:
        return counter["J"]
    return 0


def is_x_of_a_kind(card, x, with_joker=False):
    card_value = card
    counter = count_cards(card_value)
    result = False
    joker = number_of_joker(counter)
    for values in counter.values():
        if (with_joker and (values + joker) == x) or (not with_joker and values == x):
            return True
    return False


def is_five_of_a_kind(card, with_joker=False):
    card_value = card
    counter = count_cards(card_value)
    condition_full_house = False
    joker = number_of_joker(counter)
    for card_symbol in counter.keys():
        value = counter[card_symbol]
        if (not with_joker and value == 5) or (with_joker and (value + joker) == 5) or (with_joker and joker == 5):
            condition_full_house = True

    return condition_full_house


def is_full_house(card, with_joker=False):
    card_value = card
    counter = count_cards(card_value)
    different_cards = 2
    if with_joker and number_of_joker(counter) > 0:
        different_cards = 3
    if len(counter.keys()) == different_cards:
        return True

    return False


def is_two_pair(card, with_joker=False):
    card_value = card
    counter = count_cards(card_value)

    different_cards = 3
    if with_joker and number_of_joker(counter) > 0:
        different_cards = 4

    if len(counter.keys()) == different_cards:
        return True

    return False


def cmp_simple_card(card1, card2):
    result = cmp_values(card1[1], card2[1])
    return result


def cmp_card(card1, card2):
    result = cmp_values(card1[2], card2[2])
    if result == 0:
        result = cmp_values(card1[3], card2[3])
    if result == 0:
        print(card1, card2)
    return result


def cmp_values(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    return -1


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
        #print("('{}', '{}')".format(card[0], card[1]));
        result = result + (rank + 1) * card[1]
    return result


if __name__ == '__main__':
    demo_file = "demo.txt"
    puzzle_file = "input.txt"
    file = demo_file
    file = puzzle_file
    part1_deck = read_cards_part1(file)
    print(f"Day 7, Part 1: {evaluate_deck(part1_deck)}")

    part2_deck = read_cards_part1(file, with_joker=True)
    print(f"Day 7, Part 2: {evaluate_deck(part2_deck)}")
#    test_card()

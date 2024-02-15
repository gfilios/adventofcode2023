from operator import itemgetter, attrgetter
from functools import cmp_to_key


def read_cards(filename: str):
    game_deck = []
    with open(filename) as f:
        line = f.readline().strip('\n')
        while line:
            values = line.split(" ")
            game_deck.append([values[0], int(values[1]), first_order(values[0])])
            line = f.readline().strip('\n')
    return game_deck


def cmp_simple_card(card1, card2):
    if card1[1] > card2[1]:
        return 1
    elif card1[1] == card2[1]:
        return 0
    return -1


def cmp_card(card1, card2):
    if card1[2] > card2[2]:
        return 1
    elif card1[2] == card2[2]:
        return 0
    return -1


def first_order(card):
    if is_x_of_a_kind(card, 5):
        return 0
    elif is_x_of_a_kind(card, 4):
        return 1
    elif is_full_house(card):
        return 2
    elif is_x_of_a_kind(card, 3):
        return 3
    elif is_two_pair(card):
        return 4
    elif is_x_of_a_kind(card, 2):
        return 5
    return 6


def is_x_of_a_kind(card, x):
    card_value = card
    counter = count_cards(card_value)
    for values in counter.values():
        if (values == x):
            return True

    return False


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
        is_two_pair_condition = (cards[0] == 2 and cards[1] == 2) or (cards[0] == 2 and cards[2] == 2) or (cards[1] == 2 and cards[2] == 2)

    return is_two_pair_condition


def count_cards(card_value):
    counter = {}
    for next_card in card_value:
        if counter.get(next_card) is None:
            counter[next_card] = 1
        else:
            counter[next_card] += 1
    return counter


def test_card():
    card = ["11111", 88]
    print(f"is_five_of_a_kind: {card[0]}=>{is_five_of_a_kind(card)}")
    card = ["11211", 88]
    print(f"is_five_of_a_kind: {card[0]}=>{is_five_of_a_kind(card)}")

    card = ["11211", 88]
    print(f"is_four_of_a_kind: {card[0]}=>{is_four_of_a_kind(card)}")
    card = ["12211", 88]
    print(f"is_four_of_a_kind: {card[0]}=>{is_four_of_a_kind(card)}")

    card = ["12221", 88]
    print(f"is_three_of_a_kind: {card[0]}=>{is_three_of_a_kind(card)}")

    card = ["14451", 88]
    print(f"is_two_of_a_kind: {card[0]}=>{is_two_of_a_kind(card)}")

    card = ["34433", 88]
    print(f"is_full_house: {card[0]}=>{is_full_house(card)}")
    card = ["32433", 88]
    print(f"is_full_house: {card[0]}=>{is_full_house(card)}")

    card = ["12233", 88]
    print(f"is_two_pair: {card[0]}=>{is_two_pair(card)}")
    card = ["22133", 88]
    print(f"is_two_pair: {card[0]}=>{is_two_pair(card)}")
    card = ["11224", 88]
    print(f"is_two_pair: {card[0]}=>{is_two_pair(card)}")



if __name__ == '__main__':
    demo_file = "demo.txt"
    puzzle_file = "input.txt"
    file = demo_file
    main_deck = read_cards(file)
    print(main_deck)
    sorted_deck = sorted(main_deck, key=cmp_to_key(cmp_card))
    print(sorted_deck)
#    test_card()

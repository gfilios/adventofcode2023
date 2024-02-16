import unittest
import day7


class FirstOrder(unittest.TestCase):
    def test_5_in_a_row(self):
        self.assertEqual(6, day7.first_order("11111"))
        self.assertEqual(5, day7.first_order("1111J"))
        self.assertEqual(6, day7.first_order("1111J", with_joker=True))
        self.assertEqual(6, day7.first_order("J1J1J", with_joker=True))

    def test_4_in_a_row(self):
        self.assertEqual(5, day7.first_order("D1111"))
        self.assertEqual(3, day7.first_order("D111J"))
        self.assertEqual(5, day7.first_order("2223J", with_joker=True))

    def test_full_house(self):
        self.assertEqual(4, day7.first_order("22332"))
        self.assertEqual(4, day7.first_order("12121"))
        self.assertEqual(4, day7.first_order("3223J", with_joker=True))

    def test_3_in_a_row(self):
        self.assertEqual(3, day7.first_order("D3332"))
        self.assertEqual(3, day7.first_order("82212"))
        self.assertEqual(3, day7.first_order("892J2", with_joker=True))

    def test_2_pairs_in_a_row(self):
        self.assertEqual(2, day7.first_order("22113"))
        self.assertEqual(2, day7.first_order("2DD88"))
        self.assertEqual(3, day7.first_order("JDT88", with_joker=True))

    def test_1_in_a_row(self):
        self.assertEqual(1, day7.first_order("22931"))
        self.assertEqual(1, day7.first_order("2DD9T"))
        self.assertEqual(1, day7.first_order("2DJ9T",  with_joker=True))


class SecondOrder(unittest.TestCase):
    #symbol_to_hex = [["A", "F"], ["K", "E"], ["Q", "D"], ["J", "C"], ["T", "B"]]
    def test_without_Joker(self):
        self.assertEqual("0x11111", day7.card_to_hex("11111"))
        self.assertEqual("0xFFFFF", day7.card_to_hex("AAAAA"))
        self.assertEqual("0xFDCBA", day7.card_to_hex("AKQJT"))

    def test_without_Joker(self):
        self.assertEqual("0x11111", day7.card_to_hex("11111", with_joker=True))
        self.assertEqual("0xFFFFF", day7.card_to_hex("AAAAA", with_joker=True))
        self.assertEqual("0xFED1B", day7.card_to_hex("AKQJT", with_joker=True))
        self.assertEqual("0xF1E1F", day7.card_to_hex("AJKJA", with_joker=True))

    def test_compare(self):
        self.assertEqual(True,day7.second_order("JKKK2" )> day7.second_order("TKKK2"))
        self.assertEqual(True,day7.second_order("JKKK2" , True)< day7.second_order("TKKK2",True))

class Demo(unittest.TestCase):
    def test_part1(self):
        demo_file = "demo.txt"
        part1_deck = day7.read_cards_part1(demo_file)
        self.assertEqual(6440 ,day7.evaluate_deck(part1_deck))

    def test_part2(self):
        demo_file = "demo.txt"
        part1_deck = day7.read_cards_part1(demo_file, with_joker=True)
        self.assertEqual(5905 ,day7.evaluate_deck(part1_deck))


if __name__ == '__main__':
    unittest.main()

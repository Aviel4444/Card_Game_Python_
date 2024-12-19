import unittest
from Card import *

class TestCard(unittest.TestCase):
    def setUp(self):
        print("this is a setUp")

    def tearDown(self):
        print("this is a tearDown")

    """__init__unit_tests"""
    def test_valid_card_value_edge_down(self):
        """test when the value and suit both equal to one, the minimum value and suit we can get"""
        card = Card(1, 3)
        self.assertEqual(card.value, 1)

    def test_valid_card_value_edge_up(self):
        """test when the value and suit are equal to their max number they can be"""
        card = Card(13, 2)
        self.assertEqual(card.value, 13)

    def test_invalid_value_type(self):
        """test if the value isn't an int, so it should be an error"""
        with self.assertRaises(TypeError):
            card = Card("aa",2)
            self.assertEqual(card,"enter numbers, not strings")

    def test_invalid_value_range_0(self):
        """test if the value is not in his range 1-13, it should be an error"""
        with self.assertRaises(ValueError):
            card = Card(0, 2)
            self.assertEqual(card,"enter number between 1-13")

    def test_invalid_value_range_14(self):
        """test if the value is not in his range 1-13, it should be an error"""
        with self.assertRaises(ValueError):
            card = Card(14, 2)
            self.assertEqual(card,"enter number between 1-13")



    def test_valid_card_suit_edge_down(self):
        """test when the value and suit both equal to one, the minimum value and suit we can get"""
        card = Card(5, 1)
        self.assertEqual(card.suit, 1)

    def test_valid_card_suit_edge_up(self):
        """test when the value and suit are equal to their max number they can be"""
        card = Card(5, 4)
        self.assertEqual(card.suit, 4)

    def test_invalid_suit_type(self):
        """test if the suit isn't an int so it should be an error"""
        with self.assertRaises(TypeError):
            card = Card(5, "aa")
            self.assertEqual(card,"enter numbers, not strings")

    def test_invalid_suit_range_0(self):
        """test if the suit is not in his range 1-4, it should be an error"""
        with self.assertRaises(ValueError):
            card = Card(5, 0)
            self.assertEqual(card,"enter number between 1-4")

    def test_invalid_suit_range_5(self):
        """test if the suit is not in his range 1-4, it should be an error"""
        with self.assertRaises(ValueError):
            card = Card(5, 5)
            self.assertEqual(card,"enter number between 1-4")




    """__gt__unit__tests"""
    def test_valid__gt__(self):
        """test should be "True" if card 1 is greater than card 2"""
        card1 = Card(10, 3)
        card2 = Card(8, 2)
        self.assertTrue(card1 > card2)

    def test_valid__gt__values_are_equal_and_suits_are_not_equal_case1(self):
        """test should be "True" if card 1 is greater than card 2  when their values are equal and card 1 suit is bigger"""
        card1 = Card(10, 4)
        card2 = Card(10, 2)
        self.assertTrue(card1 > card2)

    def test_valid__gt__values_are_equal_and_suits_are_not_equal_case2(self):
        """test should be "False" if card 2 is greater than card 1 when their values are equal and card 1 suit is bigger"""
        card1 = Card(10, 4)
        card2 = Card(10, 2)
        self.assertFalse(card2 > card1)

    def test_valid__gt__value_is_1_case1(self):
        card1 = Card(1,4)
        card2 = Card(2,4)
        self.assertTrue(card1 > card2)

    def test_valid__gt__value_is_1_case2(self):
        card1 = Card(2, 4)
        card2 = Card(1, 4)
        self.assertTrue(card2 > card1)

    def test_invalid__gt__value_is_1_case1(self):
        card1 = Card(1,4)
        card2 = Card(2,4)
        self.assertFalse(card1 < card2)

    def test_invalid__gt__value_is_1_case2(self):
        card1 = Card(2, 4)
        card2 = Card(1, 4)
        self.assertFalse(card2 < card1)

    def test_invalid__gt__values_and_suits_are_equal(self):
        """test should be "False" if both cards values and suits are equal when card 1 is bigger"""
        card1 = Card(7, 2)
        card2 = Card(7, 2)
        self.assertFalse(card1 > card2)

    def test_invalid__gt__type(self):
        """test when both value and suit are not int, it should be an error"""
        with self.assertRaises(TypeError):
            card = Card("a", "a")
            self.assertEqual(card,f"{card} is not card")

    def test_invalid__gt__other_type(self):
        """test """
        with self.assertRaises(TypeError):
            card = Card(13,4)
            self.assertNotEqual(card,[])




    """eq_unit_tests"""
    def test_valid__eq__(self):
        """test should be "True" if both cards values and suits are equal"""
        card1 = Card(13,4)
        card2 = Card(13,4)
        self.assertTrue(card1 == card2)

    def test_invalid__eq__different_values(self):
        """test should be "False" if both cards suits are equal and values aren't equal"""
        card1 = Card(11, 1)
        card2 = Card(13, 1)
        self.assertFalse(card1 == card2)

    def test_invalid__eq__different_suits(self):
        """test should be "False" if both cards values are equal and suits aren't equal"""
        card1 = Card(13, 1)
        card2 = Card(13, 4)
        self.assertFalse(card1 == card2)

    def test_invalid__eq__other_type(self):
        with self.assertRaises(TypeError):
            card = Card(1,4)
            self.assertNotEqual(card,[])




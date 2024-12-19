import unittest
from game_cards.DeckOfCards import *


class TestDeckOfCards(unittest.TestCase):

    def setUp(self):
        """represent variables that we can use in oer test for cleaner code"""
        self.deck = DeckOfCards()


    def tearDown(self):
        print("this is tearDown")


    """init_unit_tests"""
    def test_valid_deck_length(self):
        """test if the length of cards deck game is equal to 52"""
        self.assertEqual(len(self.deck.card_deck), 52)

    def test_valid_deck_no_duplicates_length(self):
        """test if we have a length of list equal to 52 with different cards, (no duplicates)"""
        unique_cards_deck = []
        for card in self.deck.card_deck:
            if type(card) != Card:
                raise TypeError("this is not a type of card")

            if card not in unique_cards_deck:
                unique_cards_deck.append(card)

        self.assertEqual(len(unique_cards_deck), 52)

    def test_invalid_deck_length(self):
        """test if the length of cards deck game isn't equal to 30"""
        self.assertNotEqual(len(self.deck.card_deck),30)




    """cards_shuffle_unit_tests"""
    def test_valid_shuffle_deck(self):
        """test with 2 decks of cards if they are different after we shuffle one of them"""
        deck_number1 = self.deck.card_deck.copy()
        self.deck.cards_shuffle()
        deck_number2 = self.deck.card_deck
        self.assertNotEqual(deck_number1 , deck_number2)

    def test_invalid_shuffle_empty_deck(self):
        """test shuffle the deck of the card game if we have an empty deck"""
        self.deck.card_deck = []
        self.assertFalse(self.deck.cards_shuffle())




    """deal_one_unit_tests"""
    def test_valid_deal_one(self):
        """test if the card we removed with "deal one" method is not in the game deck"""
        removed_card = self.deck.deal_one()
        self.assertNotIn(removed_card,self.deck.card_deck)

    def test_valid_deal_one_length_of_deck_changed(self):
        """test if the length of the game deck is different after we deleted one card with "deal one" method"""
        original_length = len(self.deck.card_deck)
        self.deck.deal_one()
        self.assertEqual(len(self.deck.card_deck), original_length - 1)




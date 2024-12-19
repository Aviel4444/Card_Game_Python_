import unittest
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from unittest import mock


class TestPlayer(unittest.TestCase):
    def setUp(self):
        """represent variables that we can use in oer test for cleaner code"""
        self.deck = DeckOfCards()
        self.player = Player("niki", 26)

    def tearDown(self):
        print("this is a tearDown")

    """init_unit_tests"""
    def test_valid_player_name(self):
        """test when the player name is a string"""
        self.player = Player("avi", 26)
        self.assertEqual(self.player.player_name, "avi")

    def test_invalid_player_name_type(self):
         """test when the player name is not a string, it should be an error"""
         with self.assertRaises(TypeError):
            self.player = Player(12345, 26)
            self.assertEqual(self.player.player_name, "enter strings, not numbers")

    def test_invalid_player_name_empty(self):
        """test when the player name is empty, it should be an error"""
        with self.assertRaises(TypeError):
            self.player = Player(None, 26)
            self.assertEqual(self.player.player_name, "enter something")


    def test_valid_num_of_cards_player_get(self):
        """test when the number of cards players gets is int"""
        self.player = Player("avi", 26)
        self.assertEqual(self.player.num_of_cards_player_get, 26)

    def test_invalid_player_num_of_cards_player_get_type(self):
         """test when the number of cards players gets isn't int, it should be an error"""
         with self.assertRaises(TypeError):
            self.player = Player("avi", "aa")
            self.assertEqual(self.player.num_of_cards_player_get, "enter numbers, not strings")

    def test_invalid_player_num_of_cards_player_get_under_10(self):
        """test when the number of cards players gets is under 10, should be 26 default"""
        self.player = Player("avi", 9)
        self.assertEqual(self.player.num_of_cards_player_get, 26)

    def test_invalid_player_num_of_cards_player_get_above_26(self):
        """test when the number of cards players gets is above 26, should be 26 default"""
        self.player = Player("avi", 27)
        self.assertEqual(self.player.num_of_cards_player_get, 26)


    def test_valid_player_card_deck(self):
        """test if the player deck is type of list"""
        self.assertEqual(self.player.player_card_deck, [])




    """set_hand_unit_tests"""
    @mock.patch('game_cards.DeckOfCards.DeckOfCards.deal_one',return_value = Card(3,4))
    def test_valid_set_hand(self,mock_deal_one):
        """test when the mock represent the "deal one" method, if the player deck length is equal 26
        with the "set hand" method and the card we gave the mock is not in the game deck"""
        self.player.set_hand(self.deck)
        self.assertEqual(len(self.player.player_card_deck), 26)

    def test_invalid_set_hand_type(self):
        """test if the game deck is not a deck (type), it should be an error"""
        with self.assertRaises(TypeError):
            self.assertTrue(self.player.set_hand(self.deck.card_deck))




    """get_card_unit_tests"""
    def test_valid_get_card_length_of_player_deck_changed(self):
        """test if the length of the player deck changed after we used "get card" method"""
        self.player.set_hand(self.deck)
        self.player.get_card()
        self.assertEqual(len(self.player.player_card_deck),25)

    def test_valid_get_card_the_card_was_picked_not_in_player_deck(self):
        """test if the card we picked after we used "get card" method is not in the player deck"""
        self.player.set_hand(self.deck)
        card_was_picked = self.player.get_card()
        self.assertNotIn(card_was_picked,self.player.player_card_deck)




    """add_card_unit_tests"""
    def test_valid_add_card(self):
        """test if the random card was deleted from the main deck is in the player deck
         after we used "add card" method to add this card"""
        random_card = self.deck.deal_one()
        self.player.add_card(random_card)
        self.assertIn(random_card, self.player.player_card_deck)

    def test_valid_add_card_player_deck_change(self):
        """test if the player deck length increase 1 after we add his deck 1 card that we took from the game deck"""
        random_card = self.deck.deal_one()
        player_deck_before = len(self.player.player_card_deck)
        self.player.add_card(random_card)
        self.assertEqual(len(self.player.player_card_deck),player_deck_before + 1)

    def test_invalid_add_card_already_exist(self):
        """test if we add card with "add card" method that already exist"""
        card = Card(1,1)
        self.player.add_card(card)
        with self.assertRaises(TypeError):
             self.player.add_card(card)

    def test_invalid_add_card_type(self):
        """test if the card type is a card and not something else, it should be an error"""
        card = []
        with self.assertRaises(TypeError):
             self.player.add_card(card)


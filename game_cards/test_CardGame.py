import unittest
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
from game_cards.CardGame import CardGame
from unittest import mock


class TestCardGame(unittest.TestCase):
    def setUp(self):
        """represent variables that we can use in oer test for cleaner code"""
        self.deck = DeckOfCards
        self.player1 = Player("shay",26)
        self.player2 = Player("avi",26)
        self.game = CardGame("shay","avi",26)

    def tearDown(self):
        print("this is a tearDown")


    """init_unit_tests"""
    def test_valid_player1_name(self):
        """test if the player 1 name is a string"""
        self.assertEqual(self.game.player1.player_name,"shay")

    def test_valid_player2_name(self):
        """test if the player 2 name is a string"""
        self.assertEqual(self.game.player2.player_name,"avi")

    def test_invalid_player1_name_type(self):
        """test when player 1 is not a string, it should be an error"""
        with self.assertRaises(TypeError):
            self.game = CardGame(1234, "avi", 26)
            self.assertEqual(self.game.player1.player_name,"player name must be str, not numbers")

    def test_invalid_player1_name_is_empty(self):
        """test when player 1 is empty, it should be an error"""
        with self.assertRaises(TypeError):
            self.game = CardGame(None, "avi", 26)
            self.assertEqual(self.game.player1.player_name,"enter a name")

    def test_invalid_player2_name_type(self):
        """test when player 2 is not a string, it should be an error"""
        with self.assertRaises(TypeError):
            self.game = CardGame("shay", 5678, 26)
            self.assertEqual(self.game.player2.player_name,"player name must be str, not numbers")

    def test_invalid_player2_name_is_empty(self):
        """test when player 2 is empty, it should be an error"""
        with self.assertRaises(TypeError):
            self.game = CardGame("shay",None,26)
            self.assertEqual(self.game.player1.player_name,"enter a name")


    def test_valid_num_of_cards_player_get(self):
        """test if the number of cards that players gets is an int"""
        self.game = CardGame("shay", "avi", 26)
        self.assertEqual(self.game.card_number,26)

    def test_invalid_num_of_cards_player_get_type(self):
        """test if the number of cards that players gets aren't int, it should be an error"""
        with self.assertRaises(TypeError):
            self.game = CardGame("shay", "avi", "aa")
            self.assertEqual(self.game.card_number, "card numbers must be numbers, not strings")

    def test_invalid_num_of_cards_player_get_under_10(self):
        """test if the number of cards that players gets is not in the range 10-26, under 10"""
        self.game = CardGame("shay", "avi", 1)
        self.assertEqual(self.game.card_number, 26)

    def test_invalid_num_of_cards_player_get_above_26(self):
        """test if the number of cards that players gets is not in the range 10-26, above 26"""
        self.game = CardGame("shay", "avi", 40)
        self.assertEqual(self.game.card_number, 26)




    """new_game_unit_tests"""
    def test_invalid_new_game_called_not_from_the_init(self):
        """test if the new game called not from the init, it should be an error"""
        with self.assertRaises(Exception):
            self.game = CardGame("shay","avi",26)
            self.game.new_game()


    @mock.patch('game_cards.CardGame.CardGame.new_game')
    def test_valid_new_game_cards_shuffled(self,mock_shuffle):
        """test with the mock that represent the "new game" method, if the cards deck of the game had shuffled"""
        self.game = CardGame("avi","shay",26)
        mock_shuffle.assert_called_once()

    @mock.patch('game_cards.Player.Player.set_hand')
    def test_valid_new_game_set_hand_for_2_players(self,mock_set_hand):
        game = CardGame("shay","avi",26)
        self.deck = DeckOfCards
        self.player1.set_hand()
        self.player1.set_hand()
        self.assertEqual(mock_set_hand.call_count,4)
        #self.assertEqual(len(self.deck),0)

    """get_winner_unit_tests"""
    def test_valid_get_winner_win(self):
        """test should be "True" if the length of player 1 deck is greater than player 2 deck"""
        self.player1 = Player("shay", 26)
        self.player2 = Player("avi", 15)

        self.player1.player_card_deck = [1] * self.player1.num_of_cards_player_get
        self.player2.player_card_deck = [1] * self.player2.num_of_cards_player_get

        result = len(self.player1.player_card_deck) > len(self.player2.player_card_deck)

        self.assertTrue(result, f"{self.player1.player_name} is the winner!!!")

    def test_invalid_get_winner_win(self):
        """test should be "False" if the length of player 2 deck is greater than player 1 deck"""
        self.player1 = Player("shay", 26)
        self.player2 = Player("avi", 15)

        result = len(self.player1.player_card_deck) < len(self.player2.player_card_deck)

        self.assertFalse(result, f"{self.player2.player_name} is the winner!!!")

    def test_valid_get_winner_tie(self):
        """test should be "True" if the length of player 1 deck is equal to player 2 deck"""
        self.player1 = Player("shay", 26)
        self.player2 = Player("avi", 26)

        result = len(self.player1.player_card_deck) == len(self.player2.player_card_deck)

        self.assertTrue(result, "It's a tie!")

    def test_invalid_get_winner_tie(self):
        """test should be "False" if the length of player 1 deck isn't equal to player 2 deck"""
        self.player1 = Player("shay", 26)
        self.player2 = Player("avi", 26)

        result = len(self.player1.player_card_deck) != len(self.player2.player_card_deck)

        self.assertFalse(result, "It's a tie!")










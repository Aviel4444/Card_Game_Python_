from game_cards.Player import *
from game_cards.DeckOfCards import *

class CardGame:
    """the init of the class represent the 2 players names and the amount of cards each of them gets"""
    def __init__(self, player1_name, player2_name, card_number=26):
        if type(card_number) != int: #card number needs to be int and not string
            raise TypeError("card numbers must be numbers, not strings")
        self.card_number = 26

        if not 10 <= card_number <= 26: #the default is 26, so numbers under 10 or above 26 will be 26
            card_number = 26

        if type(player1_name) and type(player2_name) != str: #player's name needs to be string and not int
            raise TypeError("player name must be str, not numbers")

        if len(player1_name) < 1 and len(player2_name) < 1: #we must enter names for the players
            raise TypeError("enter a name")
        self.player1 = Player(player1_name, card_number)
        self.player2 = Player(player2_name, card_number)

        self.card_deck = DeckOfCards()

        self.start_game = True
        self.new_game()
        self.start_game = False


    def new_game(self):
        """this method represent the game, first shuffle the main card deck and after set hand the cards for
        each player"""
        if self.start_game:  #if "True"
            self.card_deck.cards_shuffle()
            self.player1.set_hand(self.card_deck)
            self.player2.set_hand(self.card_deck)
        else:
            raise Exception("game has already started, can start only from the init!!!")


    def get_winner(self):
        """this method represent the winner of the game measured by the length of cards
        , if it's a tie so it will be returned "None" """
        if len(self.player1.player_card_deck) > len(self.player2.player_card_deck):
            return self.player1.player_name
        elif len(self.player1.player_card_deck) < len(self.player2.player_card_deck):
            return self.player2.player_name
        return None



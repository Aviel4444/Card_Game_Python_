from game_cards.Card import Card
from random import shuffle, choice, randint

class DeckOfCards:
    def __init__(self):
        """the init of the class represent the game card deck that contain all 52 different cards"""
        self.card_deck = []  #creating a list
        for value in range(1,14):
            for suit in range(1,5):
                self.card_deck.append(Card(value,suit))


    def __repr__(self):
        """repr that gives us information about our deck that contains all 52 different cards"""
        return f"the deck of cards are: {self.card_deck}"


    def cards_shuffle(self):
        """with shuffle function we shuffle our card desk that we created"""
        shuffle(self.card_deck) #function that "shuffle" the cards


    def deal_one(self):
        """ with this method we can see if our deck has more than 1 card and if it has,
         we pick random card and delete him from the deck and show this card"""
        random_card = choice(self.card_deck)  # pick random card
        self.card_deck.remove(random_card)  # delete this card from the deck
        return random_card  # shows the card that got picked







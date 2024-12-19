from game_cards.DeckOfCards import *
from game_cards.Card import Card
from random import choice

class Player:
    def __init__(self, player_name, num_of_cards_player_get = 26):
        """the init of the class that represent a player name,
         the amount of cards he gets and his own deck"""

        if not type(player_name) == str: #player name should be str and not int
            raise TypeError("enter strings, not numbers")
        if len(player_name) < 1: #player name needs to be filled and not empty
            raise TypeError("enter something")
        self.player_name = player_name

        if not type(num_of_cards_player_get) == int: #number of player cards are int and not str
            raise TypeError("enter numbers, not strings")
        if not 10 <= num_of_cards_player_get <= 26 : #the cards number must be between 10-26
            num_of_cards_player_get = 26
        self.num_of_cards_player_get = num_of_cards_player_get

        self.player_card_deck = [] #represent the deck of the player


    def __repr__(self):
        """the repr return the player name and the amount of cards we will give him"""
        return f"player name is {self.player_name}, and the amount of cards he is having is {self.num_of_cards_player_get}"

    def set_hand(self,game_card_deck:DeckOfCards):
        """with this method we can get random card from the main cards deck and only if it's having cards,
         and give it to the player cards deck in the range the card number the player should get,
           after we add this random card we delete him from the main cards deck"""
        if type(game_card_deck) != DeckOfCards: #check if the card is type card from the main deck
            raise TypeError("this is not a deck of cards")

        for i in range(self.num_of_cards_player_get): #this loop will run all over the number of player card
            random_card = game_card_deck.deal_one() #pick a random card delete this card from the main card deck
            self.player_card_deck.append(random_card) #add this card to the player own card deck


    def get_card(self):
        """with this method we pick random card from player card deck if it's having cards and delete him
        from the player deck, and after that we show the deleted card"""
        random_card_from_player_package = choice(self.player_card_deck) #pick random card from the deck
        self.player_card_deck.remove(random_card_from_player_package) #remove the card wad picked from the player deck
        return random_card_from_player_package


    def add_card(self, card:Card):
        """this method gets random card from the main cards deck and add this card to the player own card deck
         and after that delete this card from the main cards deck"""
        if type(card) != Card: #check if the card is type of card
            raise TypeError("this is not a card")

        if card in self.player_card_deck:
            raise TypeError("this card already exist")
        self.player_card_deck.append(card)


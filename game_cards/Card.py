class Card:
    def __init__(self,value, suit):
        """the init of the class represent a card that contain value and suit"""
        if type(value) != int:  #value needs to be int and nor str
            raise TypeError("enter numbers, not strings")
        if value < 1 or value > 13:  #the value range is between 1-13
            raise ValueError("enter number between 1-13")
        self.value = value

        if type(suit) != int:   #suits needs to be int and nor str
            raise TypeError("enter numbers, not strings")
        if suit < 1 or suit > 4:  #the suit range is between 1-4
            raise ValueError("enter number between 1-4")
        self.suit = suit


    def __repr__(self):
        """repr that gives all the different values and suits according to their numbers"""
        self.the_card_values = {1: "ace", 2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"jack",12:"queen👸",13:"king🤴"}
        self.the_card_suits = {1:"diamonds♦️",2:"spade♠️",3:"heart♥️",4:"club♣️"}

        return f"[{self.the_card_values[self.value]} - {self.the_card_suits[self.suit]}]" #we get here the value and suit in comfortable way


    def __gt__(self, other):
        """gt gets a card and comparing between the value and suit between her own card and the card she got
             and return "True" if it gets higher card and "False" if not"""
        if type(other) != Card: #check if it's a type of card
            raise TypeError("other's card is not card")

        if self.value == other.value: #if both values are equal so we need compare between suits

            return self.suit > other.suit #if the card suit we have bigger than the card suit we got it's "True"

        if self.value == 1: #value that equal to 1 is the biggest card
            return True

        if other.value == 1: #value that equal to 1 is the biggest card
            return False

        return self.value > other.value #if our value greater than value we got so it's "True" else it's "False"


    def __eq__(self, other):
        """eq gets a card and comparing between the value and suit between her own card and the card she got
        and return "True" if they are equal and "False" if they are not"""
        if type(other) != Card: #check if it's a type of card
            raise TypeError(f"{other} is not card")
        if self.value == other.value and self.suit == other.suit:  #values and suits both equals
            return True



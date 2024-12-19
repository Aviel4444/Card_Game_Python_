import time
from game_cards.CardGame import *

def main():
    print("🤖---connecting to the server---🤖")
    time.sleep(1)
    """the main function represent the game"""
    each_player_amount_of_cards = int(input("enter a number of cards between 10-26: ")) #choose the number of cards each player will get
    player1_name = input("enter player 1 name: ") #name of player 1
    player2_name = input("enter player 2 name: ") #name of player 2

    player_1_won_numbers = 0
    player_2_won_numbers = 0

    card_game = CardGame(player1_name, player2_name,each_player_amount_of_cards) #represent the game with the 2 players
    # and the amount of cards each one gets
    print(f"welcome to the game, {card_game.player1}") #represent player 1 name and the amount of cards he has
    time.sleep(0.5)
    print(f"welcome to the game, {card_game.player2}") #represent player 2 name and the amount of cards he has
    time.sleep(1)
    print("the rules are:\n"
          "-i want a fair fight between two of you\n"
          "-the player who gets the higher card win the round\n"
          "-don't worry guys, we will try not to make to much pressure on you\n"
          "good luck!!😊")
    time.sleep(2)

    while card_game: #while the game is running
        for i in range(10):
            """play the game 10 times"""
            time.sleep(1) #how much seconds to wait between round and round
            print(f"-----round number {i + 1}-----") #every round the number increase in 1
            if i == 5:
                print("ohhhh, it's close...., who is going to win")

            time.sleep(1)
            player1_card_was_picked = card_game.player1.get_card() #player 1 get a card from the player hand
            print(f"{player1_name} is picking a card")
            time.sleep(1)
            print(f"{card_game.player1.player_name} picked {player1_card_was_picked}") #show the card was picked
            time.sleep(1)
            player2_card_was_picked = card_game.player2.get_card() #player 2 get a card from the player hand
            print(f"{player2_name} is picking a card")
            time.sleep(1)
            print(f"{card_game.player2.player_name} picked {player2_card_was_picked}") #show the card was picked


            if player1_card_was_picked > player2_card_was_picked: #if player 1 card is greater so he takes player 2 card and his card
                card_game.player1.add_card(player1_card_was_picked)
                card_game.player1.add_card(player2_card_was_picked)
                player_1_won_numbers += 1
                time.sleep(1)
                print("calculating the round 🧮")
                time.sleep(1)
                print(f"{player1_name} won this round 🏆")

            elif player1_card_was_picked < player2_card_was_picked: #if player 2 card is greater so he takes player 1 card and his card
                card_game.player2.add_card(player2_card_was_picked)
                card_game.player2.add_card(player1_card_was_picked)
                player_2_won_numbers += 1
                time.sleep(1)
                print("calculating the round 🧮")
                time.sleep(2)
                print(f"{player2_name} won this round 🏆")

        if player_1_won_numbers > player_2_won_numbers: #brings how many rounds the player who won, won
            winner_score = player_1_won_numbers
        elif player_2_won_numbers > player_1_won_numbers:
            winner_score = player_2_won_numbers
        else:
            return None

        print(f"{card_game.get_winner()} won {winner_score}/10 times") #call the "get_winner" function to see the result

        break


if __name__ =='__main__':
   main()



#This is a simple program about blackjack gamein Python. The program uses OO programming to define classes: Card, Deck, Hand, Player, User, and Computer. It also uses the logging module to write to a file named "game.log".#

##I use blackjack rules: https://www.cs.mcgill.ca/~rwest/wikispeedia/wpcd/wp/b/Blackjack.htm##

1. Program starts by running the play_game() function, which creates a deck, shuffles it, and deals two cards to both the player and the computer. 
2. After that program asks player to hit or stay until their hand value exceeds 21 or chose to stay. If the player's hand value is 21, he wins. 
3. After user has completed their turn, the computer takes their turn, hitting until their hand value exceeds 17. 
4. After that program compares the hand values of the user and computer to determine the winner.

* How to start a program:
    `#RRGGBB` `python main.py`
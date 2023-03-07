import random
import logging
from cards import suits, ranks, card_values

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = card_values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

# dealing card from the deck and after that we remove it from the deck
    def deal_card(self):
        return self.cards.pop()

#getting (player or oponent) hand from the deck
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = sum(card.value for card in self.cards)
        num_aces = sum(card.rank == 'Ace' for card in self.cards)
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value

    def __str__(self):
        return ' and '.join(str(card) for card in self.cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def add_card_to_hand(self, card):
        self.hand.add_card(card)

    def get_hand_value(self):
        return self.hand.get_value()

    def __str__(self):
        return f"{self.name} hand: {self.hand}"

class User(Player):
    def __init__(self, name):
        super().__init__(name)

class Computer(Player):
    def __init__(self):
        super().__init__('Computer')

def play_game():
    logging.info('Generating deck...')
    deck = Deck()

    # writing the cards in the deck to the log
    for card in deck.cards:
        logging.debug(card)

    deck.shuffle()

    # writing the shuffled deck to the log
    logging.debug('\n Generating deck after shuffling:\n')
    for card in deck.cards:
        logging.debug(card)
    
    user =  User(user_name)
    computer = Computer()

    for _ in range(2):
        user.add_card_to_hand(deck.deal_card())
        computer.add_card_to_hand(deck.deal_card())

    get_hand_value_user = user.get_hand_value()
    get_hannd_value_computer = computer.get_hand_value()

    # writing the rest of deck cards to the log
    logging.debug('\n Just checking how many cards left after cards added to hand:\n')
    for card in deck.cards:
        logging.debug(card)

    print(f'{user}, hand value: {get_hand_value_user}')
    print(f'{computer}, hand value: {get_hannd_value_computer}')



if __name__ == '__main__':
    #using logging to write to a file named "game.log"
    logging.basicConfig(level=logging.DEBUG,filename='game.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

    print('Welcome to Blackjack game!')
    user_name = input('Enter your name: ')
    answer = input('Do you want to play blackjack? (yes or no) ')
    
    if answer.lower() == "yes":
        play_game()
    else:
        print('Thanks for your time!')
        logging.info('Person didnt play the game')

#need to write a function to check if the user has won the game or not
#need to make user to be able to hit or stay
#need to update with error handling

import random
import logging
from cards import suits, ranks, card_values

# using logging to write to a file named "game.log"
logging.basicConfig(level=logging.DEBUG, filename='game.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = card_values[rank]

    def __str__(self) -> str:
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
    def deal_card(self) -> Card:
        return self.cards.pop()

#getting (player or oponent) hand from the deck
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: str):
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
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()

    def add_card_to_hand(self, card: str):
        self.hand.add_card(card)

    def get_hand_value(self):
        return self.hand.get_value()

    def __str__(self):
        return f"\n{self.name} hand: {self.hand}"

class User(Player):
    def __init__(self, name: str):
        super().__init__(name)
    
    def hit_or_stay(self, deck: str):
        while True:
            try:
                if self.get_hand_value() == 21:
                    print(f" THATS BLACKJACK! {self.name} wins!")
                    return False
                decision = input("Do you want to hit or stay? \n")
                if decision.lower() == "hit":
                    self.add_card_to_hand(deck.deal_card())
                    print(f"\n{self}, hand value: {self.get_hand_value()}\n")
                    if self.get_hand_value() > 21:
                        print("Over 21! Computer wins.\n")
                        return False
                elif decision.lower() == "stay":
                    return True
                else:
                    raise ValueError('Invalid input. Please enter \'hit\' or \'stay\'.\n')
            except Exception as e:
                print(f'Error: {e}')
                logging.error(f'An error occurred: {e}')


class Computer(Player):
    def __init__(self):
        super().__init__('Computer')
    
def play_game():
    try:
        logging.info('Generating deck...')
        deck = Deck()

        # writing the cards in the deck to the log
        for card in deck.cards:
            logging.debug(card)

        deck.shuffle()

        # writing the shuffled deck to the log
        logging.debug('\n  Deck after shuffling:\n')
        for card in deck.cards:
            logging.debug(card)
        
        user =  User(user_name)
        computer = Computer()

        card_count = 0
        for _ in range(2):
            card_count += 1
            user.add_card_to_hand(deck.deal_card())
            logging.debug(f"{card_count} {user.name} card: {user.hand}")
            computer.add_card_to_hand(deck.deal_card())
            logging.debug(f"{card_count} computer card: {computer.hand}")
                    
        get_hand_value_user = user.get_hand_value()
        get_hannd_value_computer = computer.get_hand_value()

        # writing the rest of deck cards to the log
        logging.debug('\n Just checking how many cards left after cards added to hand:\n')
        for card in deck.cards:
            logging.debug(card)

        print(f'{user}, hand value: {get_hand_value_user}')
        print(f'{computer}, hand value: {get_hannd_value_computer}')

        if get_hand_value_user == 21:
            print(f"{user} wins.\n")
            return
        
        if user.hit_or_stay(deck):
            while computer.get_hand_value() < 17:
                computer.add_card_to_hand(deck.deal_card())
            print(f"{user}, hand value: {user.get_hand_value()}\n")
            print(f"{computer}, hand value: {computer.get_hand_value()}\n")
            if computer.get_hand_value() > 21:
                print(f"Over 21! {user} wins.\n")
            elif computer.get_hand_value == 21:
                print(f"BLACK JACK. Computer wins.\n")
            elif computer.get_hand_value() > user.get_hand_value():
                print("Computer wins.\n")
            elif computer.get_hand_value() == user.get_hand_value():
                print("Tie!")
            else:
                print(f"{user} wins.\n")

    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    try:
        print('Welcome to Blackjack game!')
        user_name = input('Enter your name: ')
        answer = input('Do you want to play blackjack? (yes or no) \n')
        
        if answer.lower() == 'yes':
            play_game()
        elif answer.lower() == 'no':
            print('Thanks for your time!')
            logging.info('Person didnt play the game')
        else:
            raise ValueError('Invalid input. Please enter \'yes\' or \'no\'.')

    except Exception as e:
        print(f'An error occurred: {e}')
        logging.error(f'An error occurred: {e}')

# my idea is to create a simple blackjack game
# rules: https://www.blackjackapprenticeship.com/how-to-play-blackjack/
import random

#defining all suits, ranks and the values of the cards
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
#defining all ranks 
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#defining the values of the cards
card_values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Quene': 10,
    'King': 10,
    'Ace': 11
}   

#generating deck of cards combining suits and ranks
def generate_full_deck():
    count = 0
    print('Generating deck...\n')
    deck = [(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    for card in deck:
        print(f'{card[1]} of {card[0]}')
        count += 1
# just in case checking how many cards are in the deck
    print(f'\nTotal cards: {count} in the deck \n')
    return deck

def get_random_card():
    random_card = random.choice(list(generate_full_deck()))
    print(f'Random card is: {random_card[1]} of {random_card[0]}')
    if random_card[1] in card_values.keys():
        print (f'Card score is {card_values[random_card[1]]}')
generate_full_deck()
get_random_card()    


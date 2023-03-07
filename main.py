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
def generate_deck():
    count = 0
    print('Generating deck...\n')
    deck = [(rank, suit) for suit in suits for rank in ranks]
#shuffled cars    
    random.shuffle(deck)
    for card in deck:
        print(card)
        count += 1
# just in case checking how many cards are in the deck
    print(f'\n cards in the deck: {count} \n')
    return deck

#generating the random card from the deck
def get_random_card():
    random_card = random.choice(generate_deck())
    return random_card

#dealing cards for player ant oponent

def get_hand():
    for _ in range(2):
        your_hand = get_random_card()
        oponent_hand = get_random_card()
        print(your_hand)
get_hand()

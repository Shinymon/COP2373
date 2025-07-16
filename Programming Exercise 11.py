import random

# This program simulates a simple 5-card poker draw:
# 1. A shuffled deck is created.
# 2. The player is dealt 5 cards.
# 3. The player can choose which cards to discard.
# 4. The discarded cards are replaced with new ones.
# 5. The final hand is displayed.

class Deck:
    def __init__(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.card_list = [f"{rank} of {suit}" for suit in suits for rank in ranks]
        random.shuffle(self.card_list)

    def deal(self):
        return self.card_list.pop()


# Function to display a hand
def show_hand(hand, label="Hand"):
    print(f"\n{label}:")
    for i, card in enumerate(hand, 1):
        print(f"{i}: {card}")
    print()


# Function to play one round of poker hand
def play_poker_hand():
    deck = Deck()
    hand = [deck.deal() for _ in range(5)]

    show_hand(hand, "Initial Hand")

    # Get user input for which cards to replace
    replace_input = input("Enter card positions to replace (1 through 5), or press Enter to keep all: ")

    if replace_input.strip():
        indices = [int(i) - 1 for i in replace_input.split() if i.isdigit() and 1 <= int(i) <= 5]
        for idx in indices:
            hand[idx] = deck.deal()

    show_hand(hand, "Final Hand")


# Run the game
play_poker_hand()
import random
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        '''Return the machine representation of the card'''
        return f"Card({self.value!r}, {self.suit!r}"

    def __str__(self):
        '''Return string representation of the card'''
        return f"{self.value} of {self.suit}"

    def __lt__(self, other):
        '''Compare Cards first by suit then by value'''
        if self.suit == other.suit:
            return self.value < other.value
        return self.suit < other.suit

    def __eq__(self, other):
        '''Check if two cards are equal first by suit then by value'''
        return self.value == other.value and self.suit == other.suit

class Deck:
    def __init__(self, values=range(1, 14), suits=('clubs', 'diamonds', 'hearts', 'spades')):
        self.card_list = []
        for suit in suits:
            for value in values:
                self.card_list.append(Card(value, suit))

    def __len__(self):
        """Return the number of cards in the deck."""
        return len(self.card_list)

    def sort(self):
        """Sort the cards in the deck."""
        self.card_list.sort()

    def __str__(self):
        """Return a string representation of the deck."""
        return ', '.join(str(card) for card in self.card_list)

    def shuffle(self):
        """Shuffle the cards in the deck."""
        random.shuffle(self.card_list)

    def draw_top(self):
        """Remove and return the top card of the deck."""
        if not self.card_list:
            raise RuntimeError("Cannot draw from an empty deck")
        return self.card_list.pop()

class Hand(Deck):
    def __init__(self, cards=None):
        """Initialize a hand with an optional list of cards."""
        if cards is not None:
            self.card_list = cards
        else:
            self.card_list = []

    def __str__(self):
        """Return a string representation of the hand."""
        return 'Hand: ' + ', '.join(str(card) for card in self.card_list)

    def play(self, card):
        """Play a card from the hand."""
        if card not in self.card_list:
            raise RuntimeError(f"Attempted to play {card} that is not in hand: {self}")
        self.card_list.remove(card)
        return card

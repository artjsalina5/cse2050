from Cards import Card, Deck, Hand

import unittest

class TestCard(unittest.TestCase):
    """Class to evaluate the performance of Card class"""
    def test_card_init(self):
        """Test the instantiation of a Card."""
        card = Card('3', 'hearts')
        self.assertEqual(card.value, '3')
        self.assertEqual(card.suit, 'hearts')

    def test_card_repr(self):
        """Test the machine representation of a Card."""
        card = Card('3', 'hearts')
        self.assertEqual(repr(card), "Card('3', 'hearts'")

    def test_card_str(self):
        """Test the human-readable representation of a Card."""
        card = Card('3', 'hearts')
        self.assertEqual(str(card), "3 of hearts")

    def test_card_lt(self):
        """Test the less-than comparison of two Cards."""
        card1 = Card('3', 'hearts')
        card2 = Card('4', 'hearts')
        self.assertTrue(card1 < card2)

    def test_card_eq(self):
        """Test the equality comparison of two Cards."""
        card1 = Card('3', 'hearts')
        card2 = Card('3', 'hearts')
        self.assertTrue(card1 == card2)

class TestDeck(unittest.TestCase):
    """Class to evaluate the performance of Deck class"""
    def setUp(self):
        """Set up a deck of cards for each test."""
        self.deck = Deck()

    def test_deck_init(self):
        """Test the initialization of a Deck."""
        self.assertEqual(len(self.deck.card_list), 52)

    def test_deck_len(self):
        """Test the length of the Deck."""
        self.assertEqual(len(self.deck), 52)

    def test_deck_sort(self):
        """Test the sorting of the Deck."""
        self.deck.shuffle()  # Shuffle first
        self.deck.sort()  # Sort it in order
        self.assertEqual(self.deck.card_list[0].suit, 'clubs')  # Assume clubs
        self.assertEqual(self.deck.card_list[0].value, 1)  # Assuming clubs value 1

    def test_deck_str(self):
        """Test the string representation of the Deck."""
        deck_str = str(self.deck)
        self.assertIsInstance(deck_str, str)
        self.assertIn('of', deck_str)

    def test_deck_shuffle(self):
        """Test the shuffle method."""
        original_deck = self.deck.card_list.copy()
        self.deck.shuffle()
        self.assertNotEqual(original_deck, self.deck.card_list)

    def test_deck_draw_top(self):
        """Test drawing the top card from the Deck."""
        top_card = self.deck.card_list[-1]
        drawn_card = self.deck.draw_top()
        self.assertEqual(top_card, drawn_card)
        self.assertEqual(len(self.deck), 51)


class TestHand(unittest.TestCase):
    """Class to evaluate the performance of Hand class"""
    def setUp(self):
        """Create a Hand instance with some Cards for testing."""
        self.hand = Hand([Card(3, 'hearts'), Card(4, 'diamonds'), Card(2, 'spades')])

    def test_hand_init(self):
        """Test the initialization of Hand with a list of Cards."""
        self.assertEqual(len(self.hand.card_list), 3, "Hand should be initialized with 3 cards")

    def test_hand_len(self):
        """Test the __len__ method to ensure it returns the correct number of cards."""
        self.assertEqual(len(self.hand), 3, "Length of hand should be 3")

    def test_hand_sort(self):
        """Test the sort method to ensure the Hand is sorted correctly."""
        self.hand.sort()
        self.assertEqual(self.hand.card_list[0].suit, 'diamonds', "First card should be of suit 'diamonds'")
        self.assertEqual(self.hand.card_list[0].value, 4, "First card should be 4 of diamonds")

    def test_hand_str(self):
        """Test the __str__ method for a correct string representation of the Hand."""
        hand_str = str(self.hand)
        self.assertIsInstance(hand_str, str)
        self.assertIn("4 of diamonds", hand_str, "String representation of hand should contain '4 of diamonds'")

    def test_hand_play(self):
        """Test the play method by playing a card from the Hand."""
        card_to_play = Card(4, 'diamonds')
        played_card = self.hand.play(card_to_play)
        self.assertEqual(played_card, card_to_play, "The played card should be the same as the card requested to play")
        self.assertEqual(len(self.hand), 2, "The hand should have one less card after playing")

    def test_play_card_not_in_hand(self):
        """Test the play method raises an error if the card is not in the Hand."""
        card_not_in_hand = Card(5, 'hearts')
        with self.assertRaises(RuntimeError):
            self.hand.play(card_not_in_hand)

if __name__ == '__main__':
    unittest.main()


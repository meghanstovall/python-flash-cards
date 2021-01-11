# -*- coding" utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Meghan Stovall
"""

import unittest
import sys, os
sys.path.append(os.path.abspath(__file__).split('python-flash-cards')[0]+"/python-flash-cards/lib")
from Card import Card
from Deck import Deck


class TestDeck(unittest.TestCase):

    def test_exists_with_cards(self):
        card1 = Card("What is the capital of Alaska", "Juneau", "Geography")
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "Stem")
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "Stem")
        cards = [card1, card2, card3]
        deck = Deck(cards)
        self.assertEqual(deck.cards, cards)
        self.assertEqual(len(deck.cards), 3)


    def test_cards_in_category(self):
        card1 = Card("What is the capital of Alaska", "Juneau", "Geography")
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "Stem")
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "Stem")
        cards = [card1, card2, card3]
        deck = Deck(cards)
        self.assertEqual(deck.cards_in_category("Stem"), [card2, card3])
        self.assertEqual(deck.cards_in_category("Geography"), [card1])
        self.assertEqual(deck.cards_in_category("Pop Culture"), [])



if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestDeck))

    runner = unittest.TextTestRunner(verbosity = 1)
    f = runner.run(suite)
    if len(f.failures)>0 and len(f.errors)>0:
        raise Exception(str(len(f.failures))+ " Failures and " + str(len(f.errors))+ " Errors")
    if len(f.failures)>0:
        raise Exception(str(len(f.failures))+ " Failures")
    if len(f.errors)>0:
        raise Exception(str(len(f.errors))+ " Errors")
    if len(f.failures) == 0 and len(f.errors) == 0:
        print("All tests passed")

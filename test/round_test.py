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
from Round import Round
from Turn import Turn


class TestRound(unittest.TestCase):

    def test_exists_with_deck_and_current_card(self):
        card1 = Card("What is the capital of Alaska", "Juneau", "Geography")
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "Stem")
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "Stem")
        cards = [card1, card2, card3]
        deck = Deck(cards)
        new_round = Round(deck)
        self.assertIsInstance(new_round, Round)
        self.assertEqual(new_round.deck, deck)
        self.assertEqual(new_round.current_card, card1)
        self.assertEqual(new_round.turns, [])
        self.assertEqual(new_round.number_correct, 0)


    def test_take_turn(self):
        card1 = Card("What is the capital of Alaska", "Juneau", "Geography")
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "Stem")
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "Stem")
        cards = [card1, card2, card3]
        deck = Deck(cards)
        new_round = Round(deck)
        new_turn = new_round.take_turn("Juneau")
        self.assertIsInstance(new_turn, Turn)
        self.assertTrue(new_turn.correct)
        self.assertEqual(new_round.turns, [new_turn])
        self.assertEqual(new_round.number_correct, 1)
        self.assertEqual(new_round.current_card, card2)

        new_turn2 = new_round.take_turn("Venus")
        self.assertEqual(len(new_round.turns), 2)
        self.assertEqual(new_round.turns[-1].feedback(), 'Incorrect.')
        self.assertEqual(new_round.number_correct, 1)
        self.assertEqual(new_round.current_card, card3)


    def test_num_correct_by_category(self):
        card1 = Card("What is the capital of Alaska", "Juneau", "Geography")
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "Stem")
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "Stem")
        cards = [card1, card2, card3]
        deck = Deck(cards)
        new_round = Round(deck)
        new_turn = new_round.take_turn("Juneau")
        new_turn2 = new_round.take_turn("Venus")

        self.assertEqual(new_round.number_correct_by_category("Geography"), 1)
        self.assertEqual(new_round.number_correct_by_category("Stem"), 0)


    def test_percent_correct_and_by_cat(self):
        card1 = Card("What is the capital of Alaska", "Juneau", "Geography")
        card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "Stem")
        card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north?", "North north west", "Stem")
        cards = [card1, card2, card3]
        deck = Deck(cards)
        new_round = Round(deck)
        new_turn = new_round.take_turn("Juneau")
        new_turn2 = new_round.take_turn("Venus")

        self.assertEqual(new_round.percent_correct(), 50.0)
        self.assertEqual(new_round.percent_correct_by_category("Geography"), 100.0)
        self.assertEqual(new_round.current_card, card3)



if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestRound))

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

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Meghan Stovall
"""

import unittest
import sys, os
sys.path.append(os.path.abspath(__file__).split('python-flash-cards')[0]+"/python-flash-cards/lib")
from Card import Card
from Turn import Turn


class TestTurn(unittest.TestCase):

    def test_exists_with_guess_and_card(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        turn = Turn("Juneau", card)
        self.assertIsInstance(turn, Turn)
        self.assertIsInstance(turn.card, Card)
        self.assertEqual(turn.guess, "Juneau")


    def test_correct_and_feedback(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        turn = Turn("Juneau", card)
        self.assertTrue(turn.correct())
        self.assertEqual(turn.feedback(), "Correct!")

        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        turn = Turn("Juno", card)
        self.assertFalse(turn.correct())
        self.assertEqual(turn.feedback(), "Incorrect.")



if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestTurn))

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

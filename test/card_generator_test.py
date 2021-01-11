# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Meghan Stovall
"""

import unittest
import sys, os
sys.path.append(os.path.abspath(__file__).split('python-flash-cards')[0]+"/python-flash-cards/lib")
from CardGenerator import CardGenerator
from Card import Card


class TestCardGenerator(unittest.TestCase):

    def test_exists_and_can_create_cards(self):
        card = Card("What is the capital of Alaska? ", "Juneau", "Geography")

        filename = "/Users/meghanstovall/Documents/projects/python-flash-cards/lib/cards.txt"
        cards = CardGenerator(filename).cards
        self.assertIsInstance(cards, list)
        self.assertIsInstance(cards[0], Card)
        self.assertEqual(len(cards), 6)




if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestCardGenerator))

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

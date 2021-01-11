# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Meghan Stovall
"""

import unittest
import sys, os
sys.path.append(os.path.abspath(__file__).split('python-flash-cards')[0]+"/python-flash-cards/lib")
from Card import Card


class TestCard(unittest.TestCase):

    def test_exists_with_question_answer_category(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")
        self.assertIsInstance(card, Card)
        self.assertEqual(card.question, "What is the capital of Alaska?")
        self.assertEqual(card.answer, "Juneau")
        self.assertEqual(card.category, "Geography")





if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestCard))

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

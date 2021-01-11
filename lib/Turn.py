# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Meghan Stovall
"""

class Turn:

    def __init__(self, guess, card):
        self.guess = guess
        self.card = card


    def correct(self):
        if self.guess == self.card.answer: return True
        return False


    def feedback(self):
        if self.correct(): return "Correct!"
        return "Incorrect."

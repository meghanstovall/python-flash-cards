# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Meghan Stovall
"""

import sys, os
sys.path.append(os.path.abspath(__file__).split('python-flash-cards')[0]+"/python-flash-cards/lib")
from Turn import Turn

class Round:

    def __init__(self, deck):
        self.deck = deck
        self.turns = []
        self.number_correct = 0
        self.current_card = deck.cards[0]
        self.cat_dictio = self.correct_by_cat_dict()


    def take_turn(self, guess):
        new_turn = Turn(guess, self.current_card)
        self.turns.append(new_turn)
        if new_turn.correct():
            self.number_correct += 1
            self.cat_dictio[new_turn.card.category] += 1
        index = self.deck.cards.index(self.current_card)
        self.current_card = self.deck.cards[index + 1]
        return new_turn


    def correct_by_cat_dict(self):
        categories = []
        for card in self.deck.cards:
            if card.category not in categories:
                categories.append(card.category)

        dictio = {}
        for cat in categories:
            dictio[cat] = 0
        return dictio


    def number_correct_by_category(self, category):
        return self.cat_dictio[category]


    def percent_correct(self):
        return (self.number_correct / float(len(self.turns))) * 100


    def percent_correct_by_category(self, category):
        return (self.number_correct_by_category(category) / float(len(self.deck.cards_in_category(category)))) * 100

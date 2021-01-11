# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Meghan Stovall
"""

from Card import Card

class CardGenerator:

    def __init__(self, filename):
        self.cards = self.get_cards(filename)


    def get_cards(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()
        cards = []
        for obj in lines:
            new_obj = obj.strip("\n").split(",")
            card = Card(new_obj[0], new_obj[1], new_obj[2])
            cards.append(card)
        return cards

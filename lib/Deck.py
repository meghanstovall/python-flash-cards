# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Meghan Stovall
"""

class Deck:

    def __init__(self, cards):
        self.cards = cards


    def cards_in_category(self, cat):
        new_cards = []
        for card in self.cards:
            if card.category == cat:
                new_cards.append(card)
        return new_cards

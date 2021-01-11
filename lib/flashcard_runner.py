# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Meghan Stovall
"""

from CardGenerator import CardGenerator
from Deck import Deck
from Round import Round

filename = "/Users/meghanstovall/Documents/projects/python-flash-cards/lib/cards.txt"
cards = CardGenerator(filename).cards

deck = Deck(cards)
new_round = Round(deck)

def start():
  print("Welcome! You're playing with {num} cards.".format(num = len(cards)))
  print("-------------------------------------------------")
  print("This is card number {num} out of {total}".format(num = cards.index(new_round.current_card) + 1, total = len(cards)))
  guess = raw_input("Question: {q}".format(q = new_round.current_card.question))
  turn = new_round.take_turn(guess)
  print(turn.feedback())


num = 0
while num < len(deck.cards):
    num += 1
    start()

print("****** Game over! ******")
percent_corr = round(new_round.percent_correct(), 2)
print("You had {correct} correct guesses out of {total} for a total score of {percent}%.".format(correct = new_round.number_correct, total = len(deck.cards), percent = percent_corr))
for key in new_round.cat_dictio:
    p_correct = round(new_round.percent_correct_by_category(key), 2)
    print("{category} - {percent}% correct".format(category = key, percent = p_correct))

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 2020

@author: Meghan Stovall
"""

from Card import Card
from Deck import Deck
from Round import Round

card1 = Card("What is the capital of Alaska? ", "Juneau", "Geography")
card2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet? ", "Mars", "Stem")
card3 = Card("Describe in words the exact direction that is 697.5 degrees clockwise from due north? ", "North north west", "Stem")
card4 = Card("What NBA team plays in Colorado? ", "Denver Nuggets", "Sports")
card5 = Card("What direction are you headed when going away from the mountains? ", "East", "Geography")
card6 = Card("What NFL team plays in Chicago? ", "Chicago Bears", "Sports")
cards = [card1, card2, card3, card4, card5, card6]

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

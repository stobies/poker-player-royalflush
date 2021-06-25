from card import *
from hand import *

import time
import random

def current_ms():
    return round(time.time() * 1000)

class MonteCarlo:

    def run(pocket_cards, community_cards, no_of_players, time_allowed):

        start_time = current_ms()
        rounds = 0
        won = 0
        while (current_ms() <= start_time + time_allowed):
            rounds += 1
            deck = Card.generateDeck()
            Card.cleanUpDeck(deck, pocket_cards, community_cards)
            my_hand = Hand(Card.generateRandomConfig(deck, community_cards, pocket_cards))
            other_hands = []

            for i in range(0, no_of_players):
                other_hands.append(Hand(Card.generateRandomConfig(deck, community_cards, [])))
        
            my_hand_is_best = True

            for oh in other_hands:
                if oh.beats(my_hand):
                    my_hand_is_best = False
                    break

            if my_hand_is_best:
                won += 1

        if rounds > 0:
            return (won / rounds, rounds)
        
        return (0,0)
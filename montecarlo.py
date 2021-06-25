
from card import *
from hand import *

import time
import random

def current_ms():
    return round(time.time() * 1000)

class MonteCarlo:

    def get_full_deck():
        deck = []
        for val in range(2, 15):
            for suite in ['D', 'H', 'S', 'C']:
                deck.append(Card(val, suite))

        return deck

    def run(pocket_cards, community_cards, no_of_players, time_allowed):

        start_time = current_ms()
        rounds = 0
        won = 0

        deck = MonteCarlo.get_full_deck()
        my_hand = Hand(random.sample(deck, 7))

        while (current_ms() <= start_time + time_allowed):
            rounds += 1

            other_hands = []

            for i in range(0, no_of_players):
                other_hands.append(Hand(random.sample(deck, 7)))
        
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

print(MonteCarlo.run([], [], 5, 1000))
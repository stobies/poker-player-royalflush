
from enum import Enum

from card import Card


class Value(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIRS = 3
    THREE = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR = 8
    STRAIGHT_FLUSH = 9

class Hand:

    def get_runs(cards, run_length):

        start = Card(0,0)
        same_count = 0
        
        runs = []

        for c in cards:
            if c.number == start.number:
                same_count += 1
            else:
                if same_count == run_length:
                    runs.append(start)
                start = c

        return runs

    def get_flush(cards):
        suit_count = { 'H' : 0, 'D' : 0, 'S' : 0, 'C' : 0}
        for c in cards:
            suit_count[c.suit] += 1

        for (suit,count) in suit_count.items():
            if count == 5:
                return True

        return False

    def get_straight(cards):
        
        last_card = cards.pop(0)
        count = 1
        for c in cards:
            if last_card.number == c.number:
                continue
            elif last_card.number + 1 == c.number:
                count += 1
                last_card = c
            else:
                return False

        return count == 5

    # def __init__(self, cards):
    #     cards = sorted(cards, lambda card: card.number)

    #     flush = Hand.get_flush(cards)
    #     straight = Hand.get_straight(cards)

    #     if flush and straight:
    #         self.value = Value.STRAIGHT_FLUSH
    #     elif straight:
    #         self.value = Value.STRAIGHT
        
    #     quad = Hand.get_runs(cards, 4)
    #     if quad:
    #         self.value = Value.FOUR
    #         self.card = quad[0]

    #     triples = Hand.get_runs(cards, 3)
    #     pairs = Hand.get_runs(cards, 2)

    #     if triples and pairs:
    #         self.value = Value.FULL_HOUSE





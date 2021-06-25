
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
                same_count = 1
                start = c

        if same_count == run_length:
            runs.append(start)

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

    def __init__(self, cards):
        cards = sorted(cards, lambda card: card.number)

        flush = Hand.get_flush(cards)
        straight = Hand.get_straight(cards)

        if flush and straight:
            self.value = Value.STRAIGHT_FLUSH
            return
        elif straight:
            self.value = Value.STRAIGHT
            return
        
        quad = Hand.get_runs(cards, 4)
        if quad:
            self.value = Value.FOUR
            return
        
        triples = Hand.get_runs(cards, 3)
        pairs = Hand.get_runs(cards, 2)

        if triples and pairs:
            self.value = Value.FULL_HOUSE
            return

        if flush:
            self.value = Value.FLUSH
            return

        if triples:
            self.value = Value.THREE
            self.triple = triples.reverse()[0]
            return

        if len(pairs) >= 2:
            self.value = Value.TWO_PAIRS
            self.pairs = pairs.reverse()
            self.kicker = cards[-1]
            return

        if pairs:
            self.value = Value.PAIR
            self.pair = pairs[0]
            self.kickers = cards.reverse()
            return
        
        self.value = Value.HIGH_CARD
        self.high_cards = cards.reverse()

    def beats(self, other):
        if self.value > other.value:
            return True
        if self.value < other.value:
            return False

        if self.value >= Value.STRAIGHT:
            # don't worry about rare hands
            return True

        if self.value == Value.THREE:
            return self.triple.value >=  other.triple.value

        if self.value == Value.TWO_PAIRS:
            if self.pairs[0].value > other.pairs[0].value:
                return True
            elif self.pairs[0].value < other.pairs[0].value:
                return False
            else:
                if self.pairs[1].value > other.pairs[1].value:
                    return True
                elif self.pairs[1].value < other.pairs[1].value:
                    return False
                else:
                    return self.kicker.value >= other.kicker.value

        if self.value == Value.PAIR:
            if self.pair.value > other.pair.value:
                return True
            elif self.pair.value < other.pair.value:
                return False
            else:
                for l,r in zip(self.kickers, other.kickers):
                    if l.value < r.value:
                        return True
                    elif l.value > r.value:
                        return False
                return True

        if self.value == Value.HIGH_CARD:
            for l,r in zip(self.high_cards, other.high_cards):
                if l.value < r.value:
                    return True
                elif l.value > r.value:
                    return False
            return True

        return True


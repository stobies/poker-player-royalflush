
from card import Card

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

        for (suit,count) in suit_count:
            if count == 5:
                return suit

        return ''

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

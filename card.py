
class Card:
    numbers = list(range(2, 15))
    suits = ['H','S','C','D']

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def getCard(self):
        return [self.number, self.suit]
    
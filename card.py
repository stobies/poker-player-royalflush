
class Card:
    numbers = list(range(2, 15))
    suits = ['H','S','C','D']

    def __init__(self):
        self.number = 0
        self.suit = 'X'

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def getCard(self):
        return [self.number, self.suit]

    def setCard(self, number, suit):
        self.number = number
        self.suit = suit

    def getCards(cardsList):
        intRanks = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        charRanks = ["J", "Q", "K", "A"]
        apiSuits = ["hearts", "spades", "clubs", "diamonds"]
        cards = []
        for card in cardsList:
            newCard = Card()
            rank = card["rank"]
            suit = card["suit"]
            cardNumber = 0
            if rank in intRanks:
                cardNumber = intRanks.index(rank) + 2
            
            if rank in charRanks:
                cardNumber = charRanks.index(rank) + 11
            
            suitIndex = apiSuits.index(suit)
            newCard.setCard(cardNumber, newCard.suits[suitIndex])
            cards.append(newCard)
        
        return cards

            



    
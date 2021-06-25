import random

class Card:
    numbers = list(range(2, 15))
    suits = ['H','S','C','D']

    def __init__(self):
        self.number = 0
        self.suit = 'X'

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __eq__(self, other):
        return self.number == other.number and self.suit == other.suit

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
            newCard = Card(0, 0)
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

    def generateRandomConfig(communityCards, playerCards):
        cardsToGenerate = 5 - len(communityCards)
        adjList = []
        for i in range(0, cardsToGenerate):
            flag = False
            while flag is False:
                rank = random.randint(2, 14)
                suit = random.randint(0, 3)
                newCard = Card(rank, Card.suits[suit])
                if not (newCard in communityCards or newCard in playerCards):
                    flag = True
                    adjList.append(newCard)
            
        
        list = communityCards + adjList
        return list
                






            



    
import random

class Card:
    numbers = list(range(2, 15))
    suits = ['H','S','C','D']

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

    def generateRandomConfig(deck, communityCards, playerCards):
        cardsToGenerate = 7 - len(communityCards) - len(playerCards)
        adjList = random.sample(deck, cardsToGenerate)
        for el in adjList:
            deck.remove(el)

        list = playerCards + communityCards + adjList 
        return list
    
    def generateDeck():
        allCards = []
        numbers = list(range(2, 15))
        suits = ['H','S','C','D']
        for number in numbers:
            for suit in suits:
                deckCard = Card(number, suit)
                allCards.append(deckCard)
        
        return allCards

    def cleanUpDeck(deck, communityCards, playerCards):
        for card in communityCards:
            if card in deck:
                deck.remove(card)

        for card in playerCards:
            if card in deck:
                deck.remove(card)          






            



    
from hand import *
from card import *
from player import *

test_game = {"tournament_id":"550d1d68cd7bd10003000003",
    "game_id":"550da1cb2d909006e90004b1",           
    "round":0,
    "bet_index":0,
    "small_blind": 10,
    "current_buy_in": 320,
    "pot": 400,
    "minimum_raise": 240,
    "dealer": 1,
    "orbits": 7,
    "in_action": 1,
    "players": [
        {
            "id": 0,
            "name": "Albert",
            "status": "active",
            "version": "Default random player",
            "stack": 1010,
            "bet": 320
        },
        {
            "id": 1,
            "name": "Bob",
            "status": "active",
            "version": "Default random player",
            "stack": 1590,
            "bet": 80,
            "hole_cards": [
                {
                    "rank": "6",
                    "suit": "hearts"
                },
                {
                    "rank": "K",
                    "suit": "spades"
                }
            ]
        },
        {
            "id": 2,
            "name": "Chuck",
            "status": "out",
            "version": "Default random player",
            "stack": 0,
            "bet": 0
        }
    ],
    "community_cards": [
        {
            "rank": "4",
            "suit": "spades"
        },
        {
            "rank": "A",
            "suit": "hearts"
        },
        {
            "rank": "6",
            "suit": "clubs"
        }
    ]
}

def test_cards(game_state):
    idx = game_state["in_action"]
    communityCards = Card.getCards(game_state["community_cards"])
    playerCards = Card.getCards(game_state["players"][idx]["hole_cards"])
    for el in communityCards:
        print(el.number, " ", el.suit, "\n")
    
    for el in playerCards:
        print(el.number, " ", el.suit, "\n")

    print("Generated cards")
    deck = Card.generateDeck()
    list = Card.generateRandomConfig(deck, communityCards, playerCards)
    for el in list:
        print(el.number, " ", el.suit, "\n")  
try:
    test_cards(test_game)
    print("success")
except:
    print("fail")


try:
    deck = Card.generateDeck()
    idx = test_game["in_action"]
    communityCards = Card.getCards(test_game["community_cards"])
    playerCards = Card.getCards(test_game["players"][idx]["hole_cards"])
    Card.cleanUpDeck(deck, communityCards, playerCards)
    for el in deck:
        print(el.number, " ", el.suit)
except:
    print("fail")


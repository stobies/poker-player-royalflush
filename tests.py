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
    state = True
    comm = game_state["community_cards"]
    ret_comm = Card.getCards(comm)
    assert len(ret_comm) == 3
    assert ret_comm[0] == {4, "S"} and ret_comm[1] == {14, "H"} and ret_comm[2] == {6, "C"}, "Received: " + str(ret_comm)

def test_hand():
    flush = [Card(2, "D"), Card(5, "D"), Card(3, "D"), Card(4, "D"), Card(8, "D"), Card(9, "H"), Card(8, "H")]
    assert Hand.get_flush(flush) == True

    straight = [Card(2, "D"), Card(3, "D"), Card(4, "D"), Card(4, "D"), Card(5, "D"), Card(6, "D"), Card(6, "D")]
    assert Hand.get_straight(straight) == True

    full_house = [Card(2, "D"), Card(2, "D"), Card(3, "D"), Card(3, "D"), Card(3, "D"), Card(4, "D"), Card(4, "D")]
    assert len(Hand.get_runs(full_house, 2)) == 2
    assert len(Hand.get_runs(full_house, 3)) == 1

def test_player(game_state):
    p = Player()
    assert p.betRequest(game_state) > 0

try:
    test_cards(test_game)
    print("\nTEST CARDS PASSED!")
except:
    print("\nTEST CARDS FAILED!")
try:
    test_hand()
    print("\nTEST HAND PASSED!")
except:
    print("\nTEST HAND FAILED!")
try:
    test_player(test_game)
    print("\nTEST PLAYER PASSED!")
except:
    print("\nTEST HAND FAILED!")
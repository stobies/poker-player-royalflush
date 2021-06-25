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
    comm.append({"rank": "K", "suit": "diamonds"})
    ret_comm = Card.getCards(comm)
    assert len(ret_comm) == 4
    assert ret_comm[3] == {13, "D"}, "Received: " + str(ret_comm)
    comm.append({"rank": "2", "suit": "clubs"})
    ret_comm = Card.getCards(comm)
    assert len(ret_comm) == 5
    assert ret_comm[4] == {2, "C"}, "Received: " + str(ret_comm)
    comm.append(game_state["players"][1]["hole_cards"])
    ret_comm = Card.getCards(comm)
    assert len(ret_comm) == 7
    assert ret_comm[5] == {6, "H"} and ret_comm[6] == {13, "S"}, "Received: " + str(ret_comm)





def test_hand():
    highcard = Hand([Card(11, "D"), Card(5, "D"), Card(3, "C"), Card(4, "D"), Card(9, "C"), Card(12, "H"), Card(8, "H")])
    assert highcard.value is Value.HIGH_CARD, print(highcard.value)
    pair = Hand([Card(11, "D"), Card(5, "D"), Card(3, "C"), Card(4, "D"), Card(9, "C"), Card(5, "H"), Card(8, "H")])
    assert pair.value is Value.PAIR, print(pair.value)
    twopair = Hand([Card(11, "D"), Card(5, "D"), Card(8, "C"), Card(4, "D"), Card(9, "C"), Card(5, "H"), Card(8, "H")])
    assert twopair.value is Value.TWO_PAIRS, print(twopair.value)
    three = Hand([Card(11, "D"), Card(5, "D"), Card(3, "C"), Card(4, "D"), Card(9, "C"), Card(5, "H"), Card(5, "S")])
    assert three.value is Value.THREE, print(three.value)
    straight = Hand([Card(2, "D"), Card(3, "S"), Card(4, "D"), Card(4, "C"), Card(5, "D"), Card(6, "H"), Card(6, "D")])
    assert straight.value == Value.STRAIGHT, print(straight.value)
    flush = Hand([Card(9, "D"), Card(5, "D"), Card(3, "D"), Card(13, "D"), Card(12, "D"), Card(2, "H"), Card(8, "H")])
    assert flush.value is Value.FLUSH, print(flush.value)
    full_house = Hand([Card(2, "D"), Card(2, "D"), Card(3, "D"), Card(3, "D"), Card(3, "D"), Card(4, "D"), Card(4, "D")])
    assert full_house.value == Value.FULL_HOUSE
    four = Hand([Card(5, "C"), Card(5, "D"), Card(3, "C"), Card(4, "D"), Card(9, "C"), Card(5, "H"), Card(5, "S")])
    assert four.value is Value.FOUR, print(four.value)
    straightflush = Hand([Card(2, "D"), Card(3, "D"), Card(4, "D"), Card(4, "D"), Card(5, "D"), Card(6, "D"), Card(6, "D")])
    assert straightflush.value == Value.STRAIGHT_FLUSH.value, print(straightflush.value)

    assert pair.beats(highcard) 
    assert twopair.beats(highcard) and twopair.beats(pair)
    assert three.beats(twopair) and three.beats(pair)
    assert straight.beats(three) and straight.beats(twopair)
    assert flush.beats(three) and flush.beats(twopair)
    assert full_house.beats(straight) and full_house.beats(flush)
    assert four.beats(straight) and four.beats(flush)
    assert straightflush.beats(straight) and straightflush.beats(four)
    
    twopair.beats(Hand([Card(11, "D"), Card(4, "D"), Card(8, "C"), Card(4, "D"), Card(9, "C"), Card(4, "H"), Card(8, "H")]))
    assert three.beats(Hand([Card(11, "D"), Card(3, "D"), Card(3, "C"), Card(4, "D"), Card(9, "C"), Card(3, "H"), Card(3, "S")]))
    assert highcard.beats(Hand([Card(11, "D"), Card(5, "D"), Card(3, "C"), Card(4, "D"), Card(9, "C"), Card(7, "H"), Card(8, "H")]))
    assert pair.beats(Hand([Card(11, "D"), Card(2, "D"), Card(3, "C"), Card(4, "D"), Card(9, "C"), Card(2, "H"), Card(8, "H")]))
    highpair = Hand([Card(11, "D"), Card(11, "D"), Card(3, "C"), Card(4, "D"), Card(9, "C"), Card(11, "H"), Card(8, "H")])
    assert highpair.beats(pair)


def test_player(game_state):
    p = Player()
    assert p.betRequest(game_state) > 0

test_cards(test_game)
try:
    test_cards(test_game)
    print("TEST CARDS PASSED!")
except:
    print("TEST CARDS FAILED!")
try:
    test_hand()
    print("TEST HAND PASSED!")
except:
    print("TEST HAND FAILED!")
try:
    test_player(test_game)
    print("TEST PLAYER PASSED!")
except:
    print("TEST PLAYER FAILED!")
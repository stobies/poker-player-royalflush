
from card import *
from hand import *
from montecarlo import *

class Player:
    VERSION = "Royal Flush v2"

    def betRequest(self, game_state):
        idx = game_state["in_action"]
        stack = game_state["players"][idx]["stack"]
        bet = 0
        min_bet = game_state["current_buy_in"] - game_state["players"][idx]["bet"]
        raise_amount = min_bet * 2

        try:
            cards = game_state["community_cards"]
            cards.append(game_state["players"][idx]["hole_cards"][0])
            cards.append(game_state["players"][idx]["hole_cards"][1])
            hand = Hand(Card.getCards(cards))
            if hand.value.value >= Value.TWO_PAIRS.value:
                bet = min_bet * 10 
            elif min_bet > 100:
                return 0
            pocket = Hand(Card.getCards(game_state["players"][idx]["hole_cards"]))
            community = Hand(Card.getCards(game_state["community_cards"]))
            win = MonteCarlo.run(pocket, community, 5, 1000)[0]
            print(win)
            # zero round
            if len(game_state["community_cards"]) == 0:
                min_chance = 0.15 # 1/7
            # first round
            if len(game_state["community_cards"]) == 3:
                min_chance = 0.20
            # second round
            if len(game_state["community_cards"]) == 4:
                min_chance = 0.30
            # third round
            if len(game_state["community_cards"]) == 5:
                min_chance = 0.40
            if win > 2 * min_chance:
                bet = min_bet + raise_amount
            elif win > min_chance:
                bet = min_bet
            else:
                bet = 0
            if win <= 0:
                bet = min_bet
        except :
            bet = min_bet
        if bet > stack:
            return stack
        return bet

    def showdown(self, game_state):
        pass


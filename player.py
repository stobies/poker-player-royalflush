
from card import *
from hand import *


class Player:
    VERSION = "Royal Flush v1"

    def betRequest(self, game_state):
        idx = game_state["in_action"]
        stack = game_state["players"][idx]["stack"]
        bet = 0
        min_bet = game_state["current_buy_in"] - game_state["players"][idx]["bet"]
        min_chance = 0.15 # 1/7

        try:
            cards = game_state["community_cards"]
            cards.append(game_state["players"][idx]["hole_cards"])
            hand = Hand(Card.getCards(cards))
            if hand.value.value >= Value.TWO_PAIRS.value:
                bet = min_bet * 10 

#            win = 0.5 # TODO: get result here
#            # first round
#            if len(game_state["community_cards"]) == 3:
#                if win > 2 * min_chance:
#                    bet = min_bet + raise_amount
#                elif win > min_chance:
#                    bet = min_bet
#                else:
#                    bet = 0
        except:
            bet = min_bet
        if bet > stack:
            return stack
        return bet

    def showdown(self, game_state):
        pass


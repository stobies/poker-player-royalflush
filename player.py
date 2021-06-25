
from card import *
from hand import *
from montecarlo import *
import signal, time
from signal import *



class Player:
    VERSION = "Royal Flush v3"

    def betRequest(self, game_state):
        idx = game_state["in_action"]
        stack = game_state["players"][idx]["stack"]
        bet = 0
        min_bet = game_state["current_buy_in"] - game_state["players"][idx]["bet"]
        raise_amount = min_bet * 2
        
        time_per_round = 100
        if game_state["round"] > 20000 / time_per_round:
            print("TIMEOUT!")
            bet = min_bet
            if bet > stack:
                return stack
            return bet

        #if True:
        try:    
            """
            cards = game_state["community_cards"]
            cards.append(game_state["players"][idx]["hole_cards"][0])
            cards.append(game_state["players"][idx]["hole_cards"][1])
            hand = Hand(Card.getCards(cards))
            if hand.value.value >= Value.TWO_PAIRS.value:
                bet = min_bet * 10 
            elif min_bet > 100:
                return 0
            """
            pocket = Card.getCards(game_state["players"][idx]["hole_cards"])
            community = Card.getCards(game_state["community_cards"])
            win = MonteCarlo.run(pocket, community, 5, time_per_round)[0]
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

            if min_bet > 200:
                return 0

            if win <= 0:
                bet = min_bet
        except :
            bet = min_bet
            print("EXCEPTION!")
        if bet > stack:
            return stack
        return bet

    def showdown(self, game_state):
        pass


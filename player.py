
from card import *
from hand import *
from montecarlo import *
import signal, time
from signal import *

total_time = 0

class Player:
    VERSION = "Royal Flush v7"

    def betRequest(self, game_state):
        idx = game_state["in_action"]
        stack = game_state["players"][idx]["stack"]
        current_bet = game_state["players"][idx]["bet"]
        bet = 0
        min_bet = game_state["current_buy_in"] - current_bet
        raise_amount = min_bet * 2
        max_bet = 500

        time_start = time.time()

        time_per_round = 50
        global total_time
        if game_state["round"] == 0:
            total_time = 0

        if total_time > 20000:
            if min_bet + current_bet > max_bet:
                return 0
            bet = min_bet
            if bet > stack:
                return stack
            return bet

        try:
            # zero round
            if len(game_state["community_cards"]) == 0:
                bet = min_bet
            else:
                cards = game_state["community_cards"].copy()
                cards.append(game_state["players"][idx]["hole_cards"][0])
                cards.append(game_state["players"][idx]["hole_cards"][1])
                hand = Hand(Card.getCards(cards))
                if hand.value.value == Value.THREE.value:
                    return stack - max_bet
                if hand.value.value >= Value.STRAIGHT.value:
                    return stack 
                pocket = Card.getCards(game_state["players"][idx]["hole_cards"])
                community = Card.getCards(game_state["community_cards"])
                win = MonteCarlo.run(pocket, community, 5, time_per_round)[0]
                # first round
                if len(game_state["community_cards"]) == 3:
                    min_chance = 0.10
                # second round
                if len(game_state["community_cards"]) == 4:
                    min_chance = 0.20
                    raise_amount = raise_amount * 2
                # third round
                if len(game_state["community_cards"]) == 5:
                    min_chance = 0.30
                    raise_amount = raise_amount * 5
                if win > 2 * min_chance:
                    bet = min_bet + raise_amount
                elif win > min_chance:
                    bet = min_bet
                else:
                    bet = 0

            if min_bet + current_bet > max_bet:
                return 0

            if win <= 0:
                bet = min_bet
        except :
            bet = min_bet
        if bet > stack:
            return stack
        
        total_time += (time.time() - time_start) * 1000

        return bet

    def showdown(self, game_state):
        pass


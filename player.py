
class Player:
    VERSION = "Royal Flush v1"

    def betRequest(self, game_state):
        idx = game_state["in_action"]
        bet = game_state["current_buy_in"] - game_state["players"][idx]["bet"]
        stack = game_state["players"][idx]["stack"]
        if bet > stack:
            return stack
        return bet

    def showdown(self, game_state):
        pass


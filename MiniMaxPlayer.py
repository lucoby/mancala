from Mancala import Mancala

class MiniMaxPlayer():
    def __init__(self, search_depth=4):
        self.search_depth = search_depth

    def action(self, game):
        best_move, utility = self.minimax(game, depth=self.search_depth, maximizing_player=True)
        return best_move

    def utility(self, game):
        if game.is_winner(self):
            return float("inf")
        elif game.is_opponent_winner(self):
            return float("-inf")
        elif game.p1 == self:
            return game.p1_mancala - game.p2_mancala
        else:
            return game.p2_mancala - game.p1_mancala

    def minimax(self, game, depth=4, maximizing_player=True):
        if depth == 0 or game.game_over():
            return 0, self.utility(game)
        turn = game.turn
        if maximizing_player:
            best_val = float("-inf")
            best_move = game.get_valid_moves()[0]
            for m in game.get_valid_moves():
                forecast_board = game.forecast_move(m)
                forecast_move, forecast_score = self.minimax(forecast_board, depth - 1, turn == forecast_board.turn)
                if forecast_score > best_val:
                    best_val = forecast_score
                    best_move = m
            return best_move, best_val
        else:
            best_val = float("inf")
            best_move = game.get_valid_moves()[0]
            for m in game.get_valid_moves():
                forecast_board = game.forecast_move(m)
                forecast_move, forecast_score = self.minimax(forecast_board, depth - 1, turn != forecast_board.turn)
                if forecast_score < best_val:
                    best_val = forecast_score
                    best_move = m
            return best_move, best_val

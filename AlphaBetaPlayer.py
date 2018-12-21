from Mancala import Mancala

class AlphaBetaPlayer():
    def __init__(self, search_depth=4):
        self.search_depth = search_depth
        self.best_move_completed = -1

    def action(self, game):
        best_move, utility = self.alphabeta(game, depth=self.search_depth, maximizing_player=True)
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

    def alphabeta(self, game, depth=float("inf"), alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        if depth == 0 or game.game_over():
            return self.utility(game)
        turn = game.turn
        if maximizing_player:
            moves = game.get_valid_moves()
            if depth == self.search_depth and self.best_move_completed != -1:
               moves.remove(self.best_move_completed)
               moves.insert(0, self.best_move_completed)
            scores = {}
            best_val = float("-inf")
            best_move = moves[0]
            for m in moves:
                forecast_board = game.forecast_move(m)
                forecast_score = self.alphabeta(forecast_board, depth - 1, alpha, beta, turn == forecast_board.turn)
                if depth == self.search_depth:
                    scores[m] = forecast_score
                if forecast_score > best_val:
                    best_val = forecast_score
                    best_move = m
                    alpha = max(alpha, best_val)
                if beta <= alpha:
                    break
            if depth != self.search_depth:
                return best_val
            else:
                return best_move, best_val
        else:
            best_val = float("inf")
            moves = game.get_valid_moves()
            for m in moves:
                forecast_board = game.forecast_move(m)
                forecast_score = self.alphabeta(forecast_board, depth - 1, alpha, beta, turn != forecast_board.turn)
                if forecast_score < best_val:
                    best_val = forecast_score
                    best_move = m
                    beta = min(beta, best_val)
                if beta <= alpha:
                    break
            return best_val
        return best_move, best_val

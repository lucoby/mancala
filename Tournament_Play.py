from Mancala import Mancala
from Random_Player import Random_Player
from MiniMaxPlayer import MiniMaxPlayer
from AlphaBetaPlayer import AlphaBetaPlayer
import numpy as np
import datetime as dt

class Tournament_Play:
    def __init__(self, n, player_1, player_2, starting_stones=4, starting_holes=7, verbose=False):
        self.n = n
        self.player_1 = player_1
        self.player_2 = player_2
        self.starting_stones = starting_stones
        self.starting_holes = starting_holes
        self.verbose = verbose

    def play(self):
        player_1_wins = 0
        player_2_wins = 0
        draws = 0
        breadth = []
        depth = []
        for i in range(self.n):
            mancala = Mancala(self.player_1, self.player_2, starting_holes=self.starting_holes, starting_stones=self.starting_stones, verbose=self.verbose)
            result = mancala.game_loop()
            player_1_wins += 1 if result == 1 else 0
            player_2_wins += 1 if result == 2 else 0
            draws += 1 if result == 0 else 0
            breadth.append(np.mean(mancala.breadth))
            depth.append(len(mancala.breadth))
            mancala = Mancala(self.player_2, self.player_1, starting_holes=self.starting_holes, starting_stones=self.starting_stones, verbose=self.verbose)
            result = mancala.game_loop()
            player_1_wins += 1 if result == 2 else 0
            player_2_wins += 1 if result == 1 else 0
            draws += 1 if result == 0 else 0
            breadth.append(np.mean(mancala.breadth))
            depth.append(len(mancala.breadth))
        print("{}-{}-{}".format(player_1_wins, player_2_wins, draws))
        print("Average # of moves per turn: {}".format(np.mean(breadth)))
        print("Average depth of game: {}".format(np.mean(depth)))


if __name__ == '__main__':
    print("alphabeta 8 vs minimax 4")
    tournament = Tournament_Play(1, AlphaBetaPlayer(search_depth=14), MiniMaxPlayer(search_depth=4), verbose=True)
    start = dt.datetime.now()
    tournament.play()
    end = dt.datetime.now()
    print(end - start)

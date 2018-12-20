from Mancala import Mancala
from Random_Player import Random_Player
import numpy as np

class Tournament_Play:
    def __init__(self, n, player_1, player_2, starting_stones=4, starting_holes=7):
        self.n = n
        self.player_1 = player_1
        self.player_2 = player_2
        self.starting_stones = starting_stones
        self.starting_holes = starting_holes

    def play(self):
        player_1_wins = 0
        breadth = []
        depth = []
        for i in range(self.n):
            mancala = Mancala(self.player_1, self.player_2, starting_holes=self.starting_holes, starting_stones=self.starting_stones)
            player_1_wins += 1 if mancala.game_loop() == 1 else 0
            breadth.append(np.mean(mancala.breadth))
            print(breadth)
            depth.append(len(mancala.breadth))
            mancala = Mancala(self.player_2, self.player_1, starting_holes=self.starting_holes, starting_stones=self.starting_stones)
            player_1_wins += 1 if mancala.game_loop() == 2 else 0
            breadth.append(np.mean(mancala.breadth))
            depth.append(len(mancala.breadth))
        print("Player 1 won {} of {} games".format(player_1_wins, self.n * 2))
        print("Average # of moves per turn: {}".format(np.mean(breadth)))
        print("Average depth of game: {}".format(np.mean(depth)))


if __name__ == '__main__':
    tournament = Tournament_Play(3, Random_Player(), Random_Player())
    tournament.play()

from Mancala import Mancala
from Random_Player import Random_Player

class Tournament_Play:
    def __init__(self, n, player_1, player_2, starting_stones=4, starting_holes=7):
        self.n = n
        self.player_1 = player_1
        self.player_2 = player_2
        self.starting_stones = starting_stones
        self.starting_holes = starting_holes

    def play(self):
        player_1_wins = 0
        for i in range(self.n):
            mancala = Mancala(self.player_1, self.player_2, starting_holes=self.starting_holes, starting_stones=self.starting_stones)
            player_1_wins += 1 if mancala.game_loop() == 1 else 0
            mancala = Mancala(self.player_2, self.player_1, starting_holes=self.starting_holes, starting_stones=self.starting_stones)
            player_1_wins += 1 if mancala.game_loop() == 2 else 0
        print("Player 1 won {} of {} games".format(player_1_wins, self.n * 2))

if __name__ == '__main__':
    tournament = Tournament_Play(500, Random_Player(), Random_Player())
    tournament.play()

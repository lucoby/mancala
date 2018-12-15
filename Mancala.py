from Human_Player import Human_Player

class Mancala():
    """
    Each player starts with `starting_stones` number of stones in each of
    their `starting_holes` number of holes across from one another and a
    mancala (scoring hole) on either side.

    The players take turns picking a hole and counter-clockwise dropping
    1 stone into each hole (including your mancala, but not the opponent's
    mancala). If the last stone drops in your mancala, you get an extra
    turn. If your last stone falls in an empty hole on your side of the
    board you capture all stones in the opponents hole that is opposite.
    """

    def __init__(self, player_1, player_2, starting_stones=4, starting_holes=7):
        self.starting_holes = starting_holes
        self.starting_stones = starting_stones
        self.player_1 = player_1
        self.player_2 = player_2
        self.reset()
        self.print_board()

    def reset(self):
        self.player_1_holes = [self.starting_stones for i in range(self.starting_holes)]
        self.player_2_holes = [self.starting_stones for i in range(self.starting_holes)]
        self.player_1_mancala = 0
        self.player_2_mancala = 0
        self.turn = 1

    def print_board(self):
        top_row = "P2   " + "".join(["%3d"%x for x in self.player_2_holes[::-1]]) + " " + "%4d"%self.player_1_mancala
        bottom_row = "%4d"%self.player_2_mancala + " " + "".join(["%3d"%x for x in self.player_1_holes]) + "   P1"
        print(top_row)
        print(bottom_row)

if __name__ == '__main__':
    mancala = Mancala(Human_Player(), Human_Player())

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

    def valid_move(self, move):
        if not 0 <= move < self.starting_holes:
            return False
        elif self.turn == 1 and self.player_1_holes[move] == 0:
            return False
        elif self.turn == 2 and self.player_2_holes[move] == 0:
            return False
        else:
            return True

    def valid_mancala(self, move):
        if self.turn == 1:
            return (self.player_1_holes[move] - move - 1) % (2 * self.starting_holes + 1) == 0
        else:
            return (self.player_2_holes[move] - move - 1) % (2 * self.starting_holes + 1) == 0

    def apply_move(self, move):
        if self.valid_move(move):
            mancala = self.valid_mancala(move)
            if self.turn == 1:
                my_board = self.player_1_holes
                opponent_board = self.player_2_holes
            else:
                my_board = self.player_2_holes
                opponent_board = self.player_1_holes
            stones = my_board[move]
            my_board[move] = 0
            idx = move - 1
            fill_my_side = True
            while stones > 0:
                if idx > -1:
                    if fill_my_side:
                        my_board[idx] += 1
                    else:
                        opponent_board[idx] += 1
                    stones -= 1
                    idx -= 1
                if idx == -1:
                    if stones > 0 and fill_my_side:
                        if self.turn == 1:
                            self.player_1_mancala += 1
                        else:
                            self.player_2_mancala += 1
                        stones -= 1
                    fill_my_side = not fill_my_side
                    idx = self.starting_holes - 1
            if not mancala:
                self.turn = self.turn % 2 + 1

    def print_board(self):
        top_row = "P2   " + "".join(["%3d"%x for x in self.player_2_holes]) + " " + "%4d"%self.player_1_mancala
        bottom_row = "%4d"%self.player_2_mancala + " " + "".join(["%3d"%x for x in self.player_1_holes[::-1]]) + "   P1"
        print(top_row)
        print(bottom_row)

if __name__ == '__main__':
    mancala = Mancala(Human_Player(), Human_Player())

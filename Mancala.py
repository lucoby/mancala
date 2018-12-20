from Human_Player import Human_Player
from Random_Player import Random_Player

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

    def __init__(self, p1, p2, starting_stones=4, starting_holes=7, verbose=False):
        self.starting_holes = starting_holes
        self.starting_stones = starting_stones
        self.p1 = p1
        self.p2 = p2
        self.verbose = verbose
        self.breadth = []
        self.reset()

    def copy(self):
        m = Mancala(self.p1, self.p2, starting_stones=self.starting_stones, starting_holes=self.starting_holes)
        m.p1_holes = [i for i in self.p1_holes]
        m.p2_holes = [i for i in self.p2_holes]
        m.p1_mancala = self.p1_mancala
        m.p2_mancala = self.p2_mancala
        m.turn = self.turn
        return m

    def reset(self):
        self.p1_holes = [self.starting_stones for i in range(self.starting_holes)]
        self.p2_holes = [self.starting_stones for i in range(self.starting_holes)]
        self.p1_mancala = 0
        self.p2_mancala = 0
        self.turn = 1

    def get_valid_moves(self):
        return [i for i in range(self.starting_holes) if self.valid_move(i)]

    def valid_move(self, move):
        if not 0 <= move < self.starting_holes:
            return False
        elif self.turn == 1 and self.p1_holes[move] == 0:
            return False
        elif self.turn == 2 and self.p2_holes[move] == 0:
            return False
        else:
            return True

    def valid_mancala(self, move):
        if self.turn == 1:
            return (self.p1_holes[move] - move - 1) % (2 * self.starting_holes + 1) == 0
        else:
            return (self.p2_holes[move] - move - 1) % (2 * self.starting_holes + 1) == 0

    def apply_move(self, move):
        if self.valid_move(move):
            mancala = self.valid_mancala(move)
            if self.turn == 1:
                my_board = self.p1_holes
                opponent_board = self.p2_holes
            else:
                my_board = self.p2_holes
                opponent_board = self.p1_holes
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
                    if stones == 1 and fill_my_side and my_board[idx] == 1:
                        self.capture(idx)
                    stones -= 1
                    idx -= 1
                if idx == -1:
                    if stones > 0 and fill_my_side:
                        if self.turn == 1:
                            self.p1_mancala += 1
                        else:
                            self.p2_mancala += 1
                        stones -= 1
                    fill_my_side = not fill_my_side
                    idx = self.starting_holes - 1
            if not mancala:
                self.turn = self.turn % 2 + 1

    def capture(self, idx):
        if self.turn == 1:
            self.p1_mancala += self.p2_holes[self.starting_holes - idx - 1]
            self.p2_holes[self.starting_holes - idx - 1] = 0
        else:
            self.p2_mancala += self.p1_holes[self.starting_holes - idx - 1]
            self.p1_holes[self.starting_holes - idx - 1] = 0

    def final_score(self, player):
        if player == self.p1:
            return self.p1_mancala + sum(self.p1_holes)
        elif player == self.p2:
            return self.p2_mancala + sum(self.p2_holes)


    def is_winner(self, player):
        if self.game_over():
            return (player == self.p1 and self.final_score(self.p1) > self.final_score(self.p2)) \
                or (player == self.p2 and self.final_score(self.p2) > self.final_score(self.p1))

    def is_opponent_winner(self, player):
        if self.game_over():
            return (player == self.p1 and self.final_score(self.p2) > self.final_score(self.p1)) \
                or (player == self.p2 and self.final_score(self.p1) > self.final_score(self.p2))

    def game_over(self):
        if self.turn == 1:
            return self.p1_holes == [0 for i in range(self.starting_holes)]
        else:
            return self.p2_holes == [0 for i in range(self.starting_holes)]

    def game_over_captures(self):
        if self.turn == 1:
            self.p2_mancala += sum(self.p2_holes)
            self.p2_holes = [0 for i in range(self.starting_holes)]
        else:
            self.p1_mancala += sum(self.p1_holes)
            self.p1_holes = [0 for i in range(self.starting_holes)]

    def game_loop(self):
        while not self.game_over():
            move = -1
            self.breadth.append(len(self.get_valid_moves()))
            while not self.valid_move(move):
                if self.verbose:
                    print("Player {} turn".format(self.turn))
                    self.print_board()
                if self.turn == 1:
                    move = self.p1.action(self)
                else:
                    move = self.p2.action(self)
            self.apply_move(move)
        self.game_over_captures()
        if self.p1_mancala > self.p2_mancala:
            if self.verbose:
                print("Player 1 wins!")
                print("{} - {}".format(self.p1_mancala, self.p2_mancala))
            return 1
        elif self.p2_mancala > self.p1_mancala:
            if self.verbose:
                print("Player 2 wins!")
                print("{} - {}".format(self.p1_mancala, self.p2_mancala))
            return 2
        else:
            if self.verbose:
                print("Draw!")
                print("{} - {}".format(self.p1_mancala, self.p2_mancala))
            return 0

    def print_board(self):
        top_row = "P2   " + "".join(["%3d"%x for x in self.p2_holes]) + " " + "%4d"%self.p1_mancala
        bottom_row = "%4d"%self.p2_mancala + " " + "".join(["%3d"%x for x in self.p1_holes[::-1]]) + "   P1"
        print(top_row)
        print(bottom_row)

if __name__ == '__main__':
    number_holes = 7
    mancala = Mancala(Human_Player(), Random_Player(number_holes), starting_holes=number_holes, verbose=True)
    mancala.print_board()
    mancala.game_loop()

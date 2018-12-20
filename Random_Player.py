import random as rand

class Random_Player():
    def __init__(self, number_holes=7):
        self.number_holes = number_holes

    def action(self, mancala):
        return rand.randint(0, self.number_holes - 1)

if __name__ == '__main__':
    player = Human_Player()
    while True:
        move = player.action()
        print(move)

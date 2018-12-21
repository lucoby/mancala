class Human_Player():
    def action(self, mancala):
        print("Input an action:")
        move = input()
        return int(move) - 1

if __name__ == '__main__':
    player = Human_Player()
    while True:
        move = player.action()
        print(move)

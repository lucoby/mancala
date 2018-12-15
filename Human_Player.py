class Human_Player():
    def action(self):
        print("Input an action:")
        moves = input()
        return [int(x) for x in moves.split(',')]

if __name__ == '__main__':
    player = Human_Player()
    while True:
        move = player.action()
        print(move)

class Human_Player():
    def action(self):
        print("Input an action:")
        move = input()
        return int(move)

if __name__ == '__main__':
    player = Human_Player()
    while True:
        move = player.action()
        print(move)

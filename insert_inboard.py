class Insert:

    def __init__(self, player, character, play_board):
        self.player = player
        self.character = character
        self.play_board = play_board

    def game(self):
        print("It's your turn," + self.player)
        while True:
            move = input("Move "+self.character+" to :")
            if self.play_board[move] == ' ':
                self.play_board[move] = self.character
                break
            else:
                print("That place is already filled.")
        return self.play_board



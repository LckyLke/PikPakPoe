from player import HumanPlayer

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for x in range (3)]
        self.current_winner = None

    def print_board(self):
        for row in self.board:
            print(row)

    def check_moves(self):
        moves = []
        for y in range(len(self.board)):
            for (i, x) in enumerate(self.board[y]):
                if x == "O" or x == "X":
                    continue
                moves.append((y,i))
        return moves

    def num_empty_fields(self):
        return len([y[x] for x in range(3) for y in self.board])

    def place_move(self, letter, pos):
        if pos <= 3:
            self.board[0][pos - 1] = letter
            self.print_board()
            return
        if pos <= 6:
            self.board[1][pos - 4] = letter
            self.print_board()
            return
        if pos <= 9:
            self.board[2][pos - 7] = letter
            self.print_board()
            return
    def check_win(self, player):
        for row in self.board:
            if row[0] == player.letter and row[1] == player.letter and row[2] == player.letter:
                return True
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player.letter:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player.letter or self.board[0][2] == self.board[1][1] == self.board[2][0] == player.letter:
            return True





def play(game, x_player, y_player):
    game.print_board()
    while game.num_empty_fields() > 0:

        x_player.set_move(game)
        if(game.check_win(x_player)):
            print(f'{x_player.letter} won the game!')
            return
        y_player.set_move(game)
        if(game.check_win(y_player)):
            print(f'{y_player.letter} won the game!')
            return

p1 = HumanPlayer('O')
p2 = HumanPlayer('X')
game1 = TicTacToe()

play(game1, p1, p2)

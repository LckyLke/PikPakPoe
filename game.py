from player import HumanPlayer
from player import BotPlayer

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for x in range (3)]
        self.current_winner = None

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for x in range (3)]

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
        return len([y[x] for x in range(3) for y in self.board if y[x] == " "])

    def place_move(self, letter, pos, doprint=False):
        if pos <= 3:
            self.board[0][pos - 1] = letter
            if doprint: self.print_board()
            return
        if pos <= 6:
            self.board[1][pos - 4] = letter
            if doprint: self.print_board()
            return
        if pos <= 9:
            self.board[2][pos - 7] = letter
            if doprint: self.print_board()
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





def play(rounds=1, doprint=False):
    choosePs = input("Choose types of player (bb for bot v bot and pp for player v player and bp for bot v player)")
    if choosePs == "pp":
        x_player = HumanPlayer()
        y_player = HumanPlayer('X')
    elif choosePs == "bp":
        x_player = HumanPlayer()
        y_player = BotPlayer('X')
    elif choosePs == 'bb':
        x_player = BotPlayer()
        y_player = BotPlayer('X')
    else:
        print('Invalid input try again!')
        play(rounds)

    xcount, ycount, drawcount = (0,0,0)


    for _ in range(rounds):
        game = TicTacToe()
        if doprint: game.print_board()
        if doprint: print('_' * 20)
        while game.num_empty_fields() > 0:
            x_player.set_move(game, doprint)
            if doprint: print("_" * 20)
            if game.check_win(x_player):
                if doprint: print(f'{x_player.letter} won the game!')
                xcount += 1
                break
            if game.num_empty_fields() == 0:
                if doprint: print("draw")
                drawcount += 1
                break
            y_player.set_move(game, doprint)
            if doprint: print("_" * 20)
            if game.check_win(y_player):
                if doprint: print(f'{y_player.letter} won the game!')
                ycount += 1
                break
        game.reset_board()





    print(f'O won {xcount} and X won {ycount}! Draws: {drawcount}')
    print(f'O won {xcount/rounds * 100}% of the time')
    print(f'X won {ycount/rounds * 100}% of the time')
    print(f'Draws: {drawcount/rounds * 100} of the time')
    print(f'sum check: {xcount + ycount + drawcount} = {rounds}')


play(int(input("Enter the amount of rounds you want to play")), True)

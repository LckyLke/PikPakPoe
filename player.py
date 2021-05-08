import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter="O"):
        super().__init__(letter)

    def set_move(self, game, doprint=True):
        moveInput = int(input(f'{self.letter}\'s turn to make a move! Input move (1-9)'))
        if moveInput not in [(tuple[0] * 3) + tuple[1] + 1 for tuple in game.check_moves()]:
            print('Sry but this move is not valid')
            self.set_move(game)
            return
        game.place_move(self.letter, moveInput, doprint)

class BotPlayer(Player):
    def __init__(self, letter="O"):
        super().__init__(letter)

    def set_move(self, game, doprint):
        moveRan = random.choice([num for num in [1,2,3,4,5,6,7,8,9] if num in [(tuple[0] * 3) + tuple[1] + 1 for tuple in game.check_moves()]])
        game.place_move(self.letter, moveRan, doprint)


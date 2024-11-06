import random
import string
from task import calculate_score, generate_multiplayer_score

BOARD_SIZE = 4

class Game:
    def __init__(self):
        self.board = self.create_board()
        self.players = []

    @staticmethod
    def create_board():
        """Generates a random 4x4 Boggle board filled with letters A-Z."""
        board = []
        for _ in range(BOARD_SIZE):
            row = [random.choice(string.ascii_uppercase) for _ in range(BOARD_SIZE)]
            board.append(row)
        return board

    def display_board(self):
        print("Board:")
        print("-------")

        for row in self.board:
            print(" ".join(row))
        print("-------")

        print()

    def play(self):
        self.display_board()


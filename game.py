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

    def get_player_words(self, player_name):
        """Collects valid words from a player."""
        words = []
        print(f"{player_name}, enter your words. Type 'STOP' to finish.")
        while True:
            word = input("Word: ").strip().upper()
            if word == 'STOP':
                break
            else:
                words.append(word.lower())
        return words

    def setup_players(self):
        num_players = int(input("Enter number of players: "))
        for i in range(num_players):
            player_name = input(f"Enter name for player {i + 1}: ")
            words = self.get_player_words(player_name)
            self.players.append({"name": player_name, "words": words})

    def play(self):
        self.display_board()
        self.setup_players()



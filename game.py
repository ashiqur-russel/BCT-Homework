import random
import string
from task import calculate_score, generate_multiplayer_score

BOARD_SIZE = 4

class Game:
    def __init__(self):
        self.board = self.create_board()
        self.players = []
        self.dictionary = self.load_dictionary('wordlist-english.txt')


    @staticmethod
    def create_board():
        """Generates a random 4x4 Boggle board filled with letters A-Z."""
        board = []
        for _ in range(BOARD_SIZE):
            row = [random.choice(string.ascii_uppercase) for _ in range(BOARD_SIZE)]
            board.append(row)
        return board

    @staticmethod
    def load_dictionary(filepath):
        """Loads dictionary words from a file for word validation."""
        with open(filepath) as f:
            return set(word.strip().lower() for word in f)

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
            if self.is_valid_word(word):
                words.append(word.lower())
        return words

    def is_valid_word(self, word):
        """Checks if a word is valid based on dictionary and board adjacency rules."""
        if len(word) < 3:
            print(f" Word should not be less than 3 character long.")
            return False
        if word.lower() not in self.dictionary:
            print(f"'{word}' is not found at word list.")
            return False

        return True

    def setup_players(self):
        while True:
            try:
                num_players = int(input("Enter number of players: "))
                if num_players <= 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        for i in range(num_players):
            player_name = input(f"Enter name for player {i + 1}: ")
            words = self.get_player_words(player_name)
            self.players.append({"name": player_name, "words": words})

    def calculate_scores(self):
        return generate_multiplayer_score(self.players)

    def display_scores(self):
        scores = self.calculate_scores()
        print("\nScores:")
        for score in scores:
            print(f"{score['name']} scored {score['score']} points")


    def play(self):
        self.display_board()
        self.setup_players()
        self.display_scores()




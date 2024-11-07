import sys
import os
import random
import string
from task import calculate_score, generate_multiplayer_score

BOARD_SIZE = 4

class Game:
    def __init__(self):
        self.board = self.create_board()
        self.players = []
        self.dictionary = self.load_dictionary()


    @staticmethod
    def create_board():
        """Generates a random 4x4 Boggle board filled with letters A-Z."""
        board = []
        for _ in range(BOARD_SIZE):
            row = [random.choice(string.ascii_uppercase) for _ in range(BOARD_SIZE)]
            board.append(row)
        return board

    @staticmethod
    def load_dictionary():
        """
        Loads dictionary words from a file for word validation.
        This implementation was adapted based on the method described in the article:
        "How to Read a Dictionary from a File" on Finxter (https://blog.finxter.com/how-to-read-a-dictionary-from-a-file/)
        """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        filename = os.path.join(base_path, "wordlist-english.txt")

        with open(filename) as f:
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
            if word.lower() in words:
                print('You have already used the word!')
                continue
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
            print(f"'{word}' is not found in word list.")
            return False

        if self.is_adjacent_word(word.upper()):
            return True

        print('Word not found at board!')
        return False

    def is_adjacent_word(self, word):
        def dfs(x, y, word, visited):
            if len(word) == 0:
                return True

            # Boundary check and letter match check
            if (x < 0 or x >= 4 or y < 0 or y >= 4 or
                    (x, y) in visited or
                    self.board[x][y] != word[0]):
                return False

            visited.add((x, y))

            # moving all 8 directions (vertical, horizontal, and diagonal) to check
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if dfs(x + dx, y + dy, word[1:], visited):
                    return True

            visited.remove((x, y))
            return False

        # Try to find the word starting from each cell on the board
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == word[0] and dfs(i, j, word, set()):
                    return True
        return False

    def setup_players(self):
        while True:
            try:
                num_players = int(input("Enter number of players: "))
                if num_players < 2:
                    print("Minimum 2 players required!")
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




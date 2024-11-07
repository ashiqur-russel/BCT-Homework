<h1 align="center">Assignment Documentation</h1>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/yourusername/boggle-game/blob/main/LICENSE" target="_blank">
  </a>
</p>

> A console-based Boggle game for multiple players, with scoring and validation based on classic Boggle rules.


## ✨ Project Structure

```plaintext
Homework-BCT/
├── game.py                   # Core Game class for handling Boggle gameplay
├── main.py                   # Entry point for starting the game
├── task.py                   # Functions for scoring based on Boggle rules
├── wordlist-english.txt      # Dictionary file for valid words
```

The assignment repository is structured into two main parts:
1. **Scoring Functions**: Handles score calculation based on the length of each word and unique entries across players.
2. **Boggle Game Implementation**: A functional Boggle game featuring random board generation, player word input, word validation, and automatic score calculation.

<hr/>

## Task 1: Scoring Functions (task.py)

This file contains functions for calculating scores based on Boggle rules:

### 1. calculate_score(words)
This function calculates the score for a list of words based on the word lengths according to Boggle scoring rules. <br> <br>
<h5>Parameters:</h5>
<li>words (list of str): A list of valid words found by a player.
</li>

<h5>Returns:</h5>
<li>words (list of str): A list of valid words found by a player.
</li>

Scoring Rules:
<li>Words with less than 3 letters score 0 points.</li>

<li>Words with 3-4 letters score 1 point.</li>
<li>Words with 5 letters score 2 points.</li>
<li>Words with 6 letters score 3 points.</li>
<li>Words with 7 letters score 5 points.</li>
<li>Words with 8 or more letters score 11 points.</li>

### Example:

```python
words = ["catty", "wampus", "bumfuzzle"]
score = calculate_score(words)  # Output: 14
```

### 2. generate_multiplayer_score(players)

This function calculates the score for multiple players, where only unique words per player count for scoring. If multiple players submit the same word, that word does not contribute to any player’s score.

<h5>Parameters:</h5>
<li>players (list of dict): A list of dictionaries, each containing:
  <ul>
    <li><strong>name</strong> (str): The player's name.</li>
    <li><strong>words</strong> (list of str): A list of words found by the player.</li>
  </ul>
</li>

<h5>Returns:</h5>
<li>list of dict: A list of dictionaries, each containing:
  <ul>
    <li><strong>name</strong> (str): The player's name.</li>
    <li><strong>score</strong> (int): The calculated score based on unique words.</li>
  </ul>
</li>

### Example:

```python
players = [
    {"name": "Lucas", "words": ["am", "bibble", "loo", "quire"]},
    {"name": "Clara", "words": ["am", "quire", "lollygag"]}
]
multiplayer_scores = generate_multiplayer_score(players)
print(multiplayer_scores)
# Output: [{'name': 'Lucas', 'score': 3}, {'name': 'Clara', 'score': 2}]

```


### Explanation:

1. **Parameters Section**: Describes the structure of the `players` list, which contains dictionaries with each player's name and their word list.
2. **Returns Section**: Specifies that the function returns a list of dictionaries with each player’s name and calculated score.
3. **Example Code Block**: Provides an example of how to use `generate_multiplayer_score`, showing input players and the expected output.

This Markdown section provides a complete explanation of the `generate_multiplayer_score` function, including a sample input and output to help clarify usage.


## Task 2: Boggle Game Implementation (game.py)

This file contains the `Game` class, which encapsulates the logic for a playable Boggle game. It includes board generation, player setup, word validation, and score calculation.

### Game Class

#### Attributes:

- **`board`**: A 4x4 grid of random letters, representing the Boggle game board.
- **`players`**: A list of players, each with a name and a list of words they found.
- **`dictionary`**: A set of valid words loaded from `wordlist-english.txt` for word validation.

---

### `__init__`

Initializes the game by generating a board and loading the dictionary file.

```python
game = Game()
# Initializes the board and loads the dictionary
```

#### Methods

  - **Attributes Initialized**:
    - `board`: Created using `create_board()`.
    - `dictionary`: Loaded using `load_dictionary()` from `wordlist-english.txt`.
  - **Example**:
    ```python
    game = Game()
    ```
### `create_board()`
Generates a random 4x4 Boggle board filled with uppercase letters A-Z.

- **Source**: Adapted from standard practices for generating random grids in Python. Refer to similar techniques on W3docs and Spark by Examples articles.
  - **Returns**:
    - `list`: A 4x4 list of randomly chosen uppercase letters.
  - **Example**:
    ```python
    game = Game()
    print(game.create_board())
    # Output: [['F', 'L', 'A', 'G'], ['M', 'O', 'U', 'N'], ...]
    ```
    
- **`load_dictionary(filepath)`**: Loads dictionary words from a file into a set for efficient word validation.
  - **Parameters**:
    - `filepath` (str): The path to the dictionary file.
  - **Source**: Adapted based on the method described in "How to Read a Dictionary from a File" on Finxter ([link](https://blog.finxter.com/how-to-read-a-dictionary-from-a-file/)).
  - **Returns**:
    - `set`: A set containing valid words for the game.
  - **Example**:
    ```python
    game = Game()
    print(game.dictionary)  # Output: {'apple', 'banana', 'cat', ...}
    ```
    
- **`display_board()`**: Displays the 4x4 board in a structured format to the console.
  - **Example**:
    ```python
    game = Game()
    game.display_board()
    # Output:
    # Board:
    # -------
    # F L A G
    # M O U N
    # K J H G
    # R T Y B
    # -------
    ```
    
- **`get_player_words(player_name)`**: Prompts the player to enter words until they type "STOP". Each word is validated against the dictionary.
  - **Parameters**:
    - `player_name` (str): The name of the player.
  - **Returns**:
    - `list`: A list of valid words entered by the player.
  - **Example**:
    ```python
    game = Game()
    words = game.get_player_words("Player1")
    print(words)  # Output: ['flag', 'mount', 'kite', ...]
    ```
    
- **`is_valid_word(word)`**: Checks if a word is at least 3 characters long and exists in the dictionary.
  - **Parameters**:
    - `word` (str): The word to be validated.
  - **Returns**:
    - `bool`: True if the word is valid, False otherwise.
  - **Example**:
    ```python
    game = Game()
    print(game.is_valid_word("flag"))  # Output: True
    print(game.is_valid_word("a"))     # Output: False
    ```
    
### `is_adjacent_word(word)`

This method checks if a given word can be formed on the Boggle board by traversing adjacent cells. The function uses Depth-First Search (DFS) to explore all possible paths from each cell on the board, ensuring each letter in the word can be reached from the previous letter through adjacency rules (horizontal, vertical, or diagonal). Each letter cell can only be used once in a single word path.

- **Source**: Adapted from the approach discussed in [Solving Boggle using Depth-First Searches and Prefix Trees](https://medium.com/@ashalabi13/solving-boggle-using-depth-first-searches-and-prefix-trees-9c3faa89ea99) and [DFS in Python](https://favtutor.com/blogs/depth-first-search-python).

#### Parameters:
- **`word`** (str): The word to be validated against the board.

#### Returns:
- **`bool`**: `True` if the word can be formed on the board by adjacent cells, `False` otherwise.

#### Example:

```python
game = Game()
game.board = [
    ['F', 'W', 'C', 'K'],
    ['R', 'H', 'E', 'A'],
    ['X', 'V', 'L', 'O'],
    ['A', 'G', 'L', 'S']
]

word = "HELLO"
is_found = game.is_adjacent_word(word)
print(is_found)  # Output: True

```

- **`setup_players()`**: Prompts the user for the number of players and their names. Calls `get_player_words()` to collect each player’s words.
  - **Example**:
    ```python
    game = Game()
    game.setup_players()
    print(game.players)
    # Output: [{'name': 'Player1', 'words': ['flag', 'mount', ...]}, ...]
    ```

- **`calculate_scores()`**: Calculates the scores for all players using `generate_multiplayer_score` from `task.py`.
  - **Returns**:
    - `list of dict`: A list of dictionaries with each player’s name and their calculated score.
  - **Example**:
    ```python
    game = Game()
    scores = game.calculate_scores()
    print(scores)  # Output: [{'name': 'Player1', 'score': 5}, ...]
    ```

- **`display_scores()`**: Displays each player's score after all rounds are complete.
  - **Example**:
    ```python
    game = Game()
    game.display_scores()
    # Output:
    # Scores:
    # Player1 scored 5 points
    # Player2 scored 8 points
    ```

- **`play()`**: Main method to run the game. Displays the board, sets up players, and displays scores at the end.
  - **Example**:
    ```python
    game = Game()
    game.play()
    ```
    

<div>

## How to Run the Game

## Prerequisites

To run or check the Boggle game, ensure you have the following installed:

- **Python 3.7 or higher**
- **IDE (Integrated Development Environment)**


### Run the Game

### 1. Download the Project

You can either download the ZIP file or clone the Git repository.

- **Option A: Unzip the Folder**
  1. Download the ZIP file of this project.
  2. Extract (unzip) the contents to a folder on your computer.

- **Option B: Clone the Git Repository**
  1. Open a terminal or command prompt.
  2. Run the following command to clone the repository:
     ```bash
     git clone https://github.com/ashiqur-russel/BCT-Homework.git
     ```
  3. Navigate into the cloned folder:
     ```bash
     cd BCT-Homework
     ```

To start the game, execute the `main.py` file.

```bash
python main.py
```
### Gameplay

- **Board Display**: A random 4x4 grid of letters will be shown.
- **Player Setup**: Enter the number of players and their names.
- **Word Entry**: Each player will enter words they find on the board. Type "STOP" when done.
- **Scoring**: The game calculates scores based on Boggle rules and displays each player’s score.

### Rules

- Words must be at least 3 characters long.
- Each letter die can only be used once per word.
- Only unique words count towards the score in multiplayer mode.

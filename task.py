# This function accepts a list of words as a parameter. It calculates a score for each word based on its length,
# sums up these scores, and returns the total score as the final value.

def calculate_score(words):
    """
    Args:
        words (list of str): A list of words to be scored.

    Returns:
        int: The total score calculated based on the length of each word.
    """
    score = 0

    for word in words:
        length = len(word)
        if length < 3:
            continue
        elif length == 3 or length == 4:
            score += 1
        elif length == 5:
            score += 2
        elif length == 6:
            score += 3
        elif length == 7:
            score += 5
        else:
            score += 11

    return score


# This function Calculate scores for multiple players in a Boggle game, where only unique words per player earn points.

def generate_multiplayer_score(players):
    """
    Args:
        players (list of dict): A list of dictionaries, each containing:
            - 'name' (str): The player's name.
            - 'words' (list of str): A list of words found by the player.

    Returns:
        list of dict: A list of dictionaries, each containing:
            - 'name' (str): The player's name.
            - 'score' (int): The calculated score based on unique words.
    """

    word_array = []
    player_list = []

    # Getting All the words from players
    word_lists = [player.get('words') for player in players]

    for lists in word_lists:
        for word in lists:
            word_array.append(word)

    # Looping through the players to get the unique word and calculate score
    for player in players:
        unique_words = []
        for word in player['words']:
            if word_array.count(word) == 1:
                unique_words.append(word)

        # Calculate score for unique words and add to player list
        player_list.append({'name': player['name'], 'score': calculate_score(unique_words)})

    return player_list



# This function accepts a list of words as a parameter. It calculates a score for each word based on its length,
# sums up these scores, and returns the total score as the final value.

def calculate_score(words):
    """
    Calculate the score for a list of words.

    This function takes a list of words, evaluates each word based on its length,
    and assigns a score according to Boggle game scoring rules. Words shorter than
    three characters are not scored. The scoring system is as follows:

    - Word length 3, 4 -> 1 point
    - Word length 5 -> 2 points
    - Word length 6 -> 3 points
    - Word length 7 -> 5 points
    - Word length 8+ -> 11 points

    Args:
        words (list of str): A list of words to be scored.

    Returns:
        int: The total score calculated based on the length of each word.

    Example:
        >>> calculate_score(['catty', 'wampus', 'am', 'bumfuzzle'])
        16
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

word_list = ['catty', 'wampus', 'am', 'bumfuzzle', 'gardyloo', 'taradiddle', 'loo', 'snickersnee',
             'widdershins', 'teabag', 'collywobbles', 'gubbins']

result = calculate_score(word_list)
print(result)

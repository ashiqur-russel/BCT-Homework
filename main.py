from task import calculate_score, generate_multiplayer_score

def main():
    word_list = ['catty', 'wampus', 'am', 'bumfuzzle', 'gardyloo', 'taradiddle', 'loo', 'snickersnee',
                 'widdershins', 'teabag', 'collywobbles', 'gubbins']

    players = [
        {"name": "Lucas",
         "words": ["am", "bibble", "loo", "malarkey", "nudiustertian", "quire", "widdershins", "xertz", "bloviate",
                   "pluto"]},
        {"name": "Clara",
         "words": ["xertz", "gardyloo", "catty", "fuzzle", "mars", "sialoquent", "quire", "lollygag", "colly",
                   "taradiddle", "snickersnee", "widdershins", "gardy"]},
        {"name": "Klaus",
         "words": ["bumfuzzle", "wabbit", "catty", "flibbertigibbet", "am", "loo", "wampus", "bibble", "nudiustertian",
                   "xertz"]},
        {"name": "Raphael",
         "words": ["bloviate", "loo", "xertz", "mars", "erinaceous", "wampus", "am", "bibble", "cattywampus"]},
        {"name": "Tom", "words": ["bibble", "loo", "snickersnee", "quire", "am", "malarkey"]}
    ]

    multiplayer_scores = generate_multiplayer_score(players)

    print(calculate_score(word_list))

    print(multiplayer_scores)


if __name__ == "__main__":
    main()


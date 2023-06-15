""" 
Hangman Game
"""
# %% Libraries
import random

# %% Assets
country_list = [
    "Argentina",
    "Australia",
    "Austria",
    "Belgium",
    "Brazil",
    "Bulgaria",
    "Canada",
    "China",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Germany",
    "Greece",
    "Hungary",
    "India",
    "Indonesia",
    "Ireland",
    "Italy",
    "Italy",
    "Japan",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Mexico",
    "Netherlands",
    "Poland",
    "Portugal",
    "Romania",
    "Russia",
    "Saudi Arabia",
    "Slovakia",
    "Slovenia",
    "South Africa",
    "South Korea",
    "Spain",
    "Sweden",
    "Turkey",
    "United Kingdom",
    "United States",
]

hangman_list = [
    """\n                        +---+
                            |
                            |
                            |
                            |
                            |
                    -----------\n""",
    """\n                        +---+
                        |   |
                            |
                            |
                            |
                            |
                    -----------\n""",
    """\n                        +---+
                        |   |
                        O   |
                            |
                            |
                            |
                    -----------\n""",
    """\n                        +---+
                        |   |
                        O   |
                        |   |
                            |
                            |
                    -----------\n""",
    """\n                        +---+
                        |   |
                        O   |
                       /|   |
                            |
                            |
                    -----------\n""",
    """\n                        +---+
                        |   |
                        O   |
                       /|\  |
                            |
                            |
                    -----------\n""",
    """\n                        +---+
                        |   |
                        O   |
                       /|\  |
                       /    |
                            |
                    -----------\n""",
    """\n                        +---+
                        |   |
                        O   |
                       /|\  |
                       /\   |
                            |
                    -----------\n""",
]
status_list = hangman_list
status_list.reverse()
# %% Functions


# Random word genertor
def random_word():
    """Generates a random word from the specified list.

    Returns:
        word(string): Random country name from list of G20 countries.
    """
    index = random.randint(0, len(country_list))
    word = country_list[index]
    return word


def display_board(word, guess_list, status):
    """Prints out the status of the game

    Args:
        word (string): Name of country to be guessed
        guess_list (list): List of correctly guessed letters
        status (int): Number of remaining attempts
    """
    print(f"Number of letters : {len(word)} letters")
    print(
        "".join(guess_list),
    )
    print(status)


def main():
    """Main function to start the game."""
    print("\nHangman Game - Guess the G20 country")
    word = random_word()
    word_list = list(word.upper())
    guess_list = ["_"] * len(word)
    status = status_list[-1]

    display_board(word, guess_list, status)

    while len(status_list) > 0:
        guess = input("Enter your guess :  ")

        if guess.upper() in word_list:
            i = 0
            index_list = []
            while guess.upper() in word_list:
                index = word_list.index(guess.upper())
                word_list[index] = 0
                index_list.append(index)

            for i in index_list:
                guess_list[i] = guess.upper()

            display_board(word, guess_list, status)
            if "_" not in guess_list:
                print("Congratulations ! You have won.")
                break

        else:
            status_list.pop()
            status = status_list[-1]
            display_board(word, guess_list, status)
            if len(status_list) == 1:
                print("\nGame Over !")
                print(f"Country : {word}")
                break


if __name__ == "__main__":
    main()

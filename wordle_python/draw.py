"""Contain a function that write results onto console"""

from . import word


def draw(user_word: word.Word) -> None:  # noqa: D102
    """Print the current result nicely formated."""
    mapped_states = {
        word.LetterState.CORRECT: "",
        word.LetterState.MISSPLACED: "?",
        word.LetterState.WRONG: "",
    }

    word_to_print = str(user_word)
    state_to_print = "".join([mapped_states[letter.state] for letter in user_word.word])

    print("-" * 11)
    print(
        "|"
        + "".join(
            [letter + separator for letter, separator in zip(word_to_print, "|" * 5)]
        )
    )
    print("-" * 11)
    print(
        "|"
        + "".join(
            [letter + separator for letter, separator in zip(state_to_print, "|" * 5)]
        )
    )
    print("-" * 11)

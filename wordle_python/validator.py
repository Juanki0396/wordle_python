"""Contains Input validation logic"""

import pathlib
import random

from . import word


class NotAllowedWord(Exception):
    """Raised when the word is not contempled in the word reference file."""

    def __init__(self, word: word.Word, message: str) -> None:
        self.word = word
        self.message = message
        super().__init__(message)


def check_word_is_valid(word: word.Word, word_file: pathlib.Path) -> None:
    """Check if a word is in the word list."""
    with open(word_file, "r") as file:
        lines = file.readlines()
    check_word = str(word)
    for example in lines:
        if example.strip().lower() == check_word.strip().lower():
            return
        print(f"{check_word} ! = {example}")
    raise NotAllowedWord(word, f"Word {word} is not in our dictionary.")


def get_word_from_user(word_file: pathlib.Path) -> word.Word | None:
    """Ask the user for a word. If len is invalid returns None"""
    try:
        user_word = word.Word.from_str(input("Insert a 5 letter word: "))
        check_word_is_valid(user_word, word_file)
    except word.WordLenghtError:
        print("Please enter a word with 5 letter.")
        user_word = None
    except NotAllowedWord:
        print("Word is not in our dictionary")
        user_word = None

    return user_word


def select_random_word(word_file: pathlib.Path) -> word.Word:
    """Selects a random word from text file."""
    with open(word_file, "r") as file:
        word_list = file.readlines()
        selected_word = word.Word.from_str(random.choice(word_list).strip())

    return selected_word

import random

from checker import Checker
from validator import InputValidator


class Wordle:
    """Manage the game logic."""

    def __init__(self):
        self.word_list = [
            "which",
            "their",
            "would",
            "there",
            "could",
            "other",
            "about",
            "great",
            "these",
            "after",
            "first",
            "never",
            "where",
            "those",
            "shall",
            "being",
            "might",
            "every",
            "think",
            "under",
            "found",
            "still",
            "while",
            "again",
            "place",
            "young",
            "years",
            "three",
            "right",
            "house",
            "whole",
            "world",
            "thing",
            "night",
            "going",
            "heard",
            "heart",
            "among",
            "asked",
            "small",
            "woman",
            "whose",
            "quite",
            "words",
            "given",
            "taken",
            "hands",
            "until",
            "since",
            "light",
        ]

    def print_instructions(self):  # noqa: D102
        print("Instructions: Learn to play alone")

    def game(self):  # noqa: D102
        self.print_instructions()
        solution = random.choice(self.word_list)
        life = 1
        win = False
        while life < 7:
            validator = InputValidator(self.word_list)
            word = validator.get_word()
            checker = Checker(word, solution)
            position_map = checker.make_checks()
            self.draw(word, position_map, life)
            if self.is_game_won(position_map):
                win = True
                break
            life = life + 1

        if win:
            print("Congratulations, you win.")
        else:
            print("Better luck next time")

    def draw(self, word, position_map, life):  # noqa: D102
        formated_word = "|".join(list(word))
        formated_position_map = "|".join(position_map)
        print(f"Try {life} of 6")
        print(formated_word)
        print("-" * len(formated_word))
        print(formated_position_map)

    def is_game_won(self, position_map):  # noqa: D102
        if position_map == "1" * 5:
            return True
        else:
            return False

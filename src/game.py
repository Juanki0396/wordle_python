import random


class Checker:
    """Contains logic to checkif a word is correct"""

    @staticmethod
    def delete_matchs(word: str, position_map: str) -> str:
        """Substitute the letters in word with a '-' if they coincide in
        position with a 1 in postion map.
        """
        if not len(word) == len(position_map):
            raise RuntimeError("Parameters must have the same lenght")

        matched_word = [
            letter if key != "1" else "-" for letter, key in zip(word, position_map)
        ]
        return "".join(matched_word)

    def __init__(self, attempt: str, solution: str):

        self.attempt = attempt
        self.solution = solution

    def check_correct_letters(self) -> str:
        """Search from the solution the letters that appear in the final answer,
        and are placed correctly.
        """
        position_map = ""

        for index, letter in enumerate(self.attempt):
            if letter == self.solution[index]:
                position_map += "1"
            else:
                position_map += "-"

        return position_map

    def check_missplaced_letters(self, preliminary_map: str) -> str:
        """Search for the letters that are present in the final answer,
        but are missplaced.
        """
        attempt = Checker.delete_matchs(self.attempt, preliminary_map)
        output = list(preliminary_map)
        solution = list(Checker.delete_matchs(self.solution, preliminary_map))

        for index, letter in enumerate(attempt):
            if letter == "-":
                continue
            if letter in solution:
                output[index] = "2"
                solution.remove(letter)
            else:
                output[index] = "0"

        return "".join(output)

    def make_checks(self) -> str:
        """Runs the checking cycle."""
        position_map = self.check_correct_letters()
        position_map = self.check_missplaced_letters(position_map)
        return position_map


# TODO Write docstrings


class InputValidator:
    """Check if input is allowed."""

    def __init__(self, word_list: list):
        self.word_list = word_list

    def get_word(self):  # noqa: D102
        return self.word

    def check_lenght(self):  # noqa: D102
        return len(self.word) == 5

    def check_validity(self):  # noqa: D102
        return self.word in self.word_list

    def request_word(self):  # noqa: D102
        self.word = input("Enter your word: ").lower()

    def make_checks(self) -> bool:  # noqa: D102
        keep_asking = not self.check_lenght() and not self.check_validity()
        if keep_asking:
            print("Word must be in the valid words list and have 5 letters.")
        return keep_asking

    def run_validation_cycle(self):  # noqa: D102
        keep_asking = True
        while keep_asking:
            self.request_word()
            keep_asking = self.make_checks()


# TODO Restructure the code


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

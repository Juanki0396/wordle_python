"""Basic wordle logic in a poor CLI"""

import pathlib

import checker
import validator
import word


class Wordle:
    """Manage the game logic."""

    def __init__(self, word_file_path: str) -> None:
        self.word_file_path = pathlib.Path(word_file_path)

    def print_instructions(self):  # noqa: D102
        print("Instructions: Learn to play alone")

    def game(self):  # noqa: D102
        self.print_instructions()
        solution = validator.select_random_word(self.word_file_path)
        attempt = 0
        win = False

        while attempt < 7:
            print(f"Attemp {attempt}")
            user_word = validator.get_word_from_user(self.word_file_path)
            user_word = checker.check_correct_letters(
                solution=solution, attempt=user_word
            )
            user_word = checker.check_missplaced_letters(
                solution=solution, attempt=user_word
            )
            self.draw(user_word)

            if user_word.is_correct:
                win = True
                break
            attempt = attempt + 1

        if win:
            print("Congratulations, you win.")
        else:
            print("Better luck next time")

    def draw(self, user_word: word.Word) -> None:  # noqa: D102
        mapped_states = {
            word.LetterState.CORRECT: "",
            word.LetterState.MISSPLACED: "?",
            word.LetterState.WRONG: "",
        }
        word_to_print = str(user_word)
        state_to_print = "".join(
            [mapped_states[letter.state] for letter in user_word.word]
        )
        print("-" * 11)
        print(
            "|"
            + "".join(
                [
                    letter + separator
                    for letter, separator in zip(word_to_print, "|" * 5)
                ]
            )
        )
        print("-" * 11)
        print(
            "|"
            + "".join(
                [
                    letter + separator
                    for letter, separator in zip(state_to_print, "|" * 5)
                ]
            )
        )
        print("-" * 11)


if __name__ == "__main__":

    path = "./src/word_list.txt"
    Wordle(path).game()

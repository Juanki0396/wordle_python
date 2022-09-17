"""Basic wordle logic in a poor CLI"""

import argparse
import pathlib

from . import checker, draw, validator

PROGRAM_NAME = "Wordle"
DESCRIPTION = "Wordle implmented as a CLI in python."
USAGE = "Guess a 5 letter word in 5 tries."
ATTEMPTS = 5
DEFAULT_PATH = pathlib.Path(__file__).parent / "word_list.txt"

# --------------------- MAIN PROGRAM ------------------------------------------

parser = argparse.ArgumentParser(
    prog=PROGRAM_NAME, description=DESCRIPTION, usage=USAGE
)
parser.add_argument(
    "--words_path",
    type=str,
    default=DEFAULT_PATH,
    help="Select the file where valid words are",
)
args = parser.parse_args()

words_path = pathlib.Path(args.words_path)

solution = validator.select_random_word(words_path)
attempt = 0
win = False


while attempt < ATTEMPTS:
    print(f"Attemp {attempt}")
    user_word = None
    while user_word is None:
        user_word = validator.get_word_from_user(words_path)
    user_word = checker.check_correct_letters(solution=solution, attempt=user_word)
    user_word = checker.check_missplaced_letters(solution=solution, attempt=user_word)
    draw.draw(user_word)

    if user_word.is_correct:
        win = True
        break
    attempt = attempt + 1

if win:
    print("Congratulations, you win.")
else:
    print("Better luck next time")

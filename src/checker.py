"""Contains the logic to check wether a word is correct or not."""
import itertools

import word


def check_correct_letters(solution: word.Word, attempt: word.Word) -> word.Word:
    """Mark correct letters from attemp. Return modified attempted word."""
    correct_letters = solution == attempt

    for letter in itertools.compress(attempt.word, correct_letters):
        letter.set_new_state(word.LetterState.CORRECT)

    return attempt


def check_missplaced_letters(solution: word.Word, attempt: word.Word) -> word.Word:
    """Mark missplaced and wrong letters. Return modified attempted word."""
    unknown_letters = solution != attempt
    attempt_unknown_letters = list(itertools.compress(attempt.word, unknown_letters))
    solution_unknown_letters = list(itertools.compress(solution.word, unknown_letters))

    for letter in attempt_unknown_letters:
        if letter in solution_unknown_letters:
            letter.set_new_state(word.LetterState.MISSPLACED)
        else:
            letter.set_new_state(word.LetterState.WRONG)

    return attempt

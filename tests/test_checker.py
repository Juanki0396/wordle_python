from wordle_python import checker, word


class TestCorrectLetters:
    """Set of tests for check_correct_letters in checker module."""

    def test_all_correct(self):
        """Check a word equal to the solution."""
        test_word = word.Word.from_str("hello")
        test_objective = word.Word.from_str("hello")
        test_word = checker.check_correct_letters(
            solution=test_objective, attempt=test_word
        )
        assert test_word.is_correct

    def test_no_match(self):
        """Check a word totally different to the solution."""
        test_word = word.Word.from_str("hello")
        test_objective = word.Word.from_str("where")
        test_word = checker.check_correct_letters(
            solution=test_objective, attempt=test_word
        )
        assert all(
            [letter.state == word.LetterState.UNKNOWN for letter in test_word.word]
        )

    def test_some_match(self):
        """Check a word with some matching letters."""
        test_word = word.Word.from_str("hello")
        test_objective = word.Word.from_str("holly")
        test_word = checker.check_correct_letters(
            solution=test_objective, attempt=test_word
        )
        matches = [
            word.LetterState.CORRECT,
            word.LetterState.UNKNOWN,
            word.LetterState.CORRECT,
            word.LetterState.CORRECT,
            word.LetterState.UNKNOWN,
        ]
        assert all(
            [
                letter.state == predict
                for letter, predict in zip(test_word.word, matches)
            ]
        )


class TestMissplacedLetters:
    """Set of tests for check_missplaced_letters in checker module."""

    def test_no_match(self):
        """Check if set wrong a non matching word."""
        test_word = word.Word.from_str("hello")
        test_objective = word.Word.from_str("zumba")
        test_word = checker.check_missplaced_letters(
            solution=test_objective, attempt=test_word
        )
        assert all(
            [letter.state == word.LetterState.WRONG for letter in test_word.word]
        )

    def test_all_match(self):
        """Check if not change the correct state of a word."""
        letters = [
            word.Letter("z", word.LetterState.CORRECT),
            word.Letter("u", word.LetterState.CORRECT),
            word.Letter("m", word.LetterState.CORRECT),
            word.Letter("b", word.LetterState.CORRECT),
            word.Letter("a", word.LetterState.CORRECT),
        ]
        test_word = word.Word(letters)
        test_objective = word.Word.from_str("zumba")
        test_word = checker.check_missplaced_letters(
            solution=test_objective, attempt=test_word
        )
        assert test_word.is_correct

    def test_some_missplacements(self):
        """Check if set correct misplacements and wrong letters."""
        letters = [
            word.Letter("z", word.LetterState.CORRECT),
            word.Letter("u", word.LetterState.CORRECT),
            word.Letter("b", word.LetterState.UNKNOWN),
            word.Letter("o", word.LetterState.UNKNOWN),
            word.Letter("m", word.LetterState.UNKNOWN),
        ]
        test_word = word.Word(letters)
        test_objective = word.Word.from_str("zumba")
        test_word = checker.check_missplaced_letters(
            solution=test_objective, attempt=test_word
        )
        matches = [
            word.LetterState.CORRECT,
            word.LetterState.CORRECT,
            word.LetterState.MISSPLACED,
            word.LetterState.WRONG,
            word.LetterState.MISSPLACED,
        ]
        assert all(
            [
                letter.state == predict
                for letter, predict in zip(test_word.word, matches)
            ]
        )

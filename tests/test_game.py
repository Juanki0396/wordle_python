from unittest import TestCase

from src.game import Checker, InputValidator


class TestChecker(TestCase):
    """Test the Checker class"""

    def setUp(self):  # noqa: D102
        solution = "error"
        attemp = "perra"
        self.checker = Checker(attemp, solution)

    def test_delete_matchs(self):  # noqa: D102
        word = "perra"
        position_map = "--1--"

        expected = "pe-ra"
        output = Checker.delete_matchs(word, position_map)

        self.assertEqual(expected, output, "Matches has not been deleted correctly")

    def test_check_correct_letters(self):  # noqa: D102
        expected = "--1--"
        output = self.checker.check_correct_letters()

        self.assertEqual(output, expected, "Position map is not as expected")

    def test_check_missplaced_letters(self):  # noqa: D102
        position_map = "--1--"

        expected = "02120"
        output = self.checker.check_missplaced_letters(position_map)

        self.assertEqual(output, expected, "Position map is not as expected")


class TestInputValidator(TestCase):
    """Checks the InputValidator class"""

    def setUp(self):  # noqa: D102
        word_list = ["hello", "wheat", "shoes", "jeans"]
        self.validator = InputValidator(word_list)

    def test_check_lenght(self):  # noqa: D102
        self.validator.word = "ratata"
        self.assertFalse(
            self.validator.check_lenght(), "This word has 6 letters, not 5."
        )
        self.validator.word = "perro"
        self.assertTrue(self.validator.check_lenght(), "This word has 5 letters")

    def test_check_validity(self):  # noqa: D102
        self.validator.word = "ratata"
        self.assertFalse(
            self.validator.check_validity(), "This word is not in the word list."
        )
        self.validator.word = "hello"
        self.assertTrue(
            self.validator.check_validity(), "This word is not in the word list."
        )


class TestWordle(TestCase):  # noqa: D101
    pass

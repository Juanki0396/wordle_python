import builtins
import pathlib

import pytest

from wordle_python import validator, word


class TestCheckWordIsValid:
    """Set of test for check_word_is_valid method."""

    def test_valid_word(self):
        """Check that any exception is raised for a valid word."""
        path = pathlib.Path("./wordle_python/word_list.txt")
        test_word = word.Word.from_str("which")
        validator.check_word_is_valid(test_word, path)

    def test_non_valid_word(self):
        """Check that a exception is raised for a non valid word."""
        path = pathlib.Path("./wordle_python/word_list.txt")
        test_word = word.Word.from_str("jamon")
        with pytest.raises(validator.NotAllowedWord):
            validator.check_word_is_valid(test_word, path)


class TestGetWordFromUser:
    """Set of test for get_word_from_user_method."""

    def test_word_lenght(self, monkeypatch):
        """Check if the output is none for a wrong lenght."""

        def mock_input(*args, **kwargs) -> str:
            return "shdahalsd"

        monkeypatch.setattr(builtins, "input", mock_input)
        path = pathlib.Path("./wordle_python/word_list.txt")
        user_word = validator.get_word_from_user(path)
        assert user_word is None

    def test_word_not_allowed(self, monkeypatch):
        """Check if the output is none for a wrong word."""

        def mock_input(*args, **kwargs) -> str:
            return "jamon"

        monkeypatch.setattr(builtins, "input", mock_input)
        path = pathlib.Path("./wordle_python/word_list.txt")
        user_word = validator.get_word_from_user(path)
        assert user_word is None

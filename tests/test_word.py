import pytest

from wordle_python import word


class TestLetter:
    """A set of tests from the Letter class."""

    def test_right_init(self):
        """Checks for correct letter initialization."""
        letter_1 = word.Letter("a")
        letter_2 = word.Letter("a", word.LetterState.WRONG)
        assert letter_1.letter == "a"
        assert letter_2.letter == "a"
        assert letter_1.state == word.LetterState.UNKNOWN
        assert letter_2.state == word.LetterState.WRONG

    def test_raise_length_error(self):
        """Checks if error raised when instanciate a letter with len != 0"""
        with pytest.raises(word.LetterLengthError):
            word.Letter("asas")

    def test_equatily(self):
        """Checks that equality operator works properly."""
        letter_1 = word.Letter("a")
        letter_2 = word.Letter("a")
        letter_3 = word.Letter("b")
        assert letter_1 == letter_2
        assert not letter_1 == letter_3

    def test_inequality(self):
        """Checks that inequality operator works fine."""
        letter_1 = word.Letter("a")
        letter_2 = word.Letter("a")
        letter_3 = word.Letter("b")
        assert not letter_1 != letter_2
        assert letter_1 != letter_3

    def test_set_new_state(self):
        """Checks if the letter state can be updated."""
        letter = word.Letter("a")
        letter.set_new_state(word.LetterState.CORRECT)
        assert letter.state == word.LetterState.CORRECT


class TestWord:
    """Set of tests from Word class."""

    def test_correct_init(self):
        """Check that the word is instanciated correctly."""
        letter_list = [word.Letter(letter) for letter in "hello"]
        test_word = word.Word(letter_list)
        for letter_w, letter_l in zip(test_word.word, letter_list):
            assert letter_w == letter_l

    def test_wrong_len(self):
        """Check that an error is raised when wrong len is passed."""
        with pytest.raises(word.WordLenghtError):
            letter_list = [word.Letter(letter) for letter in "hello_world"]
            word.Word(letter_list)

    def test_init_from_str(self):
        """Check that a word is correctly created from a string."""
        letter_list = [word.Letter(letter) for letter in "hello"]
        test_word = word.Word(letter_list)
        test_word_from_str = word.Word.from_str("hello")
        for letter_1, letter_2 in zip(test_word.word, test_word_from_str.word):
            assert letter_1 == letter_2

    def test_equality(self):
        """Check that equality works as expected."""
        letter_list_1 = [word.Letter(letter) for letter in "hello"]
        letter_list_2 = [word.Letter(letter) for letter in "hollo"]
        test_word_1 = word.Word(letter_list_1)
        test_word_2 = word.Word(letter_list_2)
        assert sum(test_word_1 == test_word_2) == 4
        assert all(test_word_1 == test_word_1)

    def test_inequality(self):
        """Check that inequality operator works as expected."""
        letter_list_1 = [word.Letter(letter) for letter in "hello"]
        letter_list_2 = [word.Letter(letter) for letter in "hollo"]
        test_word_1 = word.Word(letter_list_1)
        test_word_2 = word.Word(letter_list_2)
        assert sum(test_word_1 != test_word_2) == 1
        assert not all(test_word_1 != test_word_1)

    def test_select_item(self):
        """Check that an item can be selected."""
        letter_list = [word.Letter(letter) for letter in "hello"]
        test_word = word.Word(letter_list)
        assert test_word[2] == word.Letter("l")

    def test_to_str(self):
        """Check that the word can be converted into a string."""
        letter_list = [word.Letter(letter) for letter in "hello"]
        test_word = word.Word(letter_list)
        assert str(test_word) == "hello"

    def test_is_correct(self):
        """Check if is_correct property is true when all letters are CORRECT."""
        letter_list_1 = [
            word.Letter(letter, word.LetterState.CORRECT) for letter in "hello"
        ]
        letter_list_2 = [word.Letter(letter) for letter in "hello"]
        test_word_1 = word.Word(letter_list_1)
        test_word_2 = word.Word(letter_list_2)
        assert test_word_1.is_correct
        assert not test_word_2.is_correct

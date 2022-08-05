from __future__ import annotations

import dataclasses
import enum


class LetterState(enum.Enum):  # noqa: D101

    UNKNOWN = enum.auto()
    WRONG = enum.auto()
    MISSPLACED = enum.auto()
    CORRECT = enum.auto()


class LetterLengthError(Exception):
    """Raised when letter length is not 1."""


class WordLenghtError(Exception):
    """Raised when word length is no 5."""


@dataclasses.dataclass
class Letter:
    """Represent a wordle letter."""

    letter: str
    state: LetterState = dataclasses.field(default=LetterState.UNKNOWN)

    def __post_init__(self) -> None:
        if len(self.letter) != 1:
            raise LetterLengthError("Letter can only have len == 1")

    def __eq__(self, letter: Letter) -> bool:
        return self.letter == letter.letter

    def __ne__(self, letter: Letter) -> bool:
        return self.letter != letter.letter

    def set_new_state(self, state: LetterState) -> None:
        """Set new state for the letter."""
        self.state = state


@dataclasses.dataclass
class Word:
    """Represent a Wordle word."""

    word: list[Letter]

    @classmethod
    def from_str(cls, word: str) -> Word:
        """Creates a Word from a string"""
        word = [Letter(letter) for letter in word]
        return cls(word)

    @property
    def is_correct(self) -> bool:
        """Returns True if all letters are correct."""
        return all([letter.state == LetterState.CORRECT for letter in self.word])

    def __post_init__(self) -> None:
        if len(self) != 5:
            raise WordLenghtError("Word should contain five letters.")

    def __len__(self) -> int:
        return len(self.word)

    def __getitem__(self, index: int) -> Letter:
        return self.word[index]

    def __eq__(self, word: Word) -> list[bool]:
        """Return an list with comparison for each letter."""
        return [
            letter_a == letter_b for letter_a, letter_b in zip(self.word, word.word)
        ]

    def __ne__(self, word: Word) -> list[bool]:
        """Return an list with opposite comparison for each letter."""
        return [
            letter_a != letter_b for letter_a, letter_b in zip(self.word, word.word)
        ]

    def __str__(self) -> str:
        return "".join([letter.letter for letter in self.word])

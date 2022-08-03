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


class Letter(dataclasses.dataclass):
    """Represent a wordle letter."""

    letter: str
    state: LetterState = dataclasses.field(default=LetterState.UNKNOWN)

    def __post_init__(self) -> None:
        if len(self.letter) != 1:
            raise LetterLengthError("Letter can only have len == 1")

    def __eq__(self, letter: Letter) -> bool:
        return self.letter == letter.letter


class Word(dataclasses.dataclass):
    """Represent a Wordle word."""

    word: list[Letter]

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

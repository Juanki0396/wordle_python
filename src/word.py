import enum


class LetterState(enum.Enum):  # noqa: D101

    UNKNOWN = enum.auto()
    WRONG = enum.auto()
    MISSPLACED = enum.auto()
    CORRECT = enum.auto()

"""Contains Input validation logic"""


class InputValidator:
    """Check if input is allowed."""

    def __init__(self, word_list: list):
        self.word_list = word_list

    def get_word(self):  # noqa: D102
        return self.word

    def check_lenght(self):  # noqa: D102
        return len(self.word) == 5

    def check_validity(self):  # noqa: D102
        return self.word in self.word_list

    def request_word(self):  # noqa: D102
        self.word = input("Enter your word: ").lower()

    def make_checks(self) -> bool:  # noqa: D102
        keep_asking = not self.check_lenght() and not self.check_validity()
        if keep_asking:
            print("Word must be in the valid words list and have 5 letters.")
        return keep_asking

    def run_validation_cycle(self):  # noqa: D102
        keep_asking = True
        while keep_asking:
            self.request_word()
            keep_asking = self.make_checks()

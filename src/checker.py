"""Contains the logic to check wether a word is correct or not."""


class Checker:
    """Contains logic to checkif a word is correct"""

    @staticmethod
    def delete_matchs(word: str, position_map: str) -> str:
        """Substitute the letters in word with a '-' if they coincide in
        position with a 1 in postion map.
        """
        if not len(word) == len(position_map):
            raise RuntimeError("Parameters must have the same lenght")

        matched_word = [
            letter if key != "1" else "-" for letter, key in zip(word, position_map)
        ]
        return "".join(matched_word)

    def __init__(self, attempt: str, solution: str):

        self.attempt = attempt
        self.solution = solution

    def check_correct_letters(self) -> str:
        """Search from the solution the letters that appear in the final answer,
        and are placed correctly.
        """
        position_map = ""

        for index, letter in enumerate(self.attempt):
            if letter == self.solution[index]:
                position_map += "1"
            else:
                position_map += "-"

        return position_map

    def check_missplaced_letters(self, preliminary_map: str) -> str:
        """Search for the letters that are present in the final answer,
        but are missplaced.
        """
        attempt = Checker.delete_matchs(self.attempt, preliminary_map)
        output = list(preliminary_map)
        solution = list(Checker.delete_matchs(self.solution, preliminary_map))

        for index, letter in enumerate(attempt):
            if letter == "-":
                continue
            if letter in solution:
                output[index] = "2"
                solution.remove(letter)
            else:
                output[index] = "0"

        return "".join(output)

    def make_checks(self) -> str:
        """Runs the checking cycle."""
        position_map = self.check_correct_letters()
        position_map = self.check_missplaced_letters(position_map)
        return position_map

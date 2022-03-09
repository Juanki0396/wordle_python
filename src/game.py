import random


class Checker():

    def __init__(self, attempt, solution):

        self.attempt = list(attempt)
        self.solution = list(solution)
        print(f'SOLUTION: {solution}')

    def check_correct_letters(self) -> list:
        """ Search from the input solution the letters that appear in the final answer, and are placed correctly.

        Returns:
            list: generates a preliminary map of the results of the input attempt:
                  1 - Corresponds to a correct letter, placed in the right place
                  '-' - Corresponds to a letter that either is part of the solution, or it is wrong
        """
        output = []
        solution = self.solution.copy()
        attempt = self.attempt.copy()
        for index, letter in enumerate(self.attempt):
            if letter == self.solution[index]:
                output.append('1')
                solution[index] = '-'
                attempt[index] = '-'
            else:
                output.append('-')
        self.attempt = attempt
        self.solution = solution
        self.position_map = output

        return output

    def check_missplaced_letters(self) -> list:
        """Search for the letters that are present in the final answer, but are missplaced.

        Returns:
            list: generates a final map of the results of the input attempt
                  2 - Corresponds to a letter that is present in the final answer, but it's missplaced. 
                  1 - Corresponds to a correct letter, placed in the right place
                  0 - Corresponds to a wrong letter
        """

        output = self.position_map.copy()
        solution = self.solution.copy()

        for index, letter in enumerate(self.attempt):
            if letter == '-':
                continue
            if letter in solution:
                output[index] = '2'
                solution.remove(letter)
            else:
                output[index] = '0'

        self.position_map = output
        return output


class Inputer():

    def __init__(self, word_list: list):
        self.word_list = word_list
        keep_asking = True
        while keep_asking:
            self.word = input('Enter your word: ').lower()
            if not self.check_lenght():
                print('The word must have 5 letters')
                continue
            if self.check_validity():
                break
            else:
                print('Word is not in the allowed solutions')

    def get_word(self):
        return self.word

    def check_lenght(self):
        if len(self.word) == 5:
            return True
        else:
            return False

    def check_validity(self):
        if self.word in self.word_list:
            return True
        else:
            return False


class Wordle():

    def __init__(self):
        self.word_list = ['which', 'their', 'would', 'there', 'could', 'other', 'about', 'great', 'these', 'after', 'first', 'never', 'where', 'those', 'shall', 'being', 'might', 'every', 'think', 'under', 'found', 'still', 'while', 'again',
                          'place', 'young', 'years', 'three', 'right', 'house', 'whole', 'world', 'thing', 'night', 'going', 'heard', 'heart', 'among', 'asked', 'small', 'woman', 'whose', 'quite', 'words', 'given', 'taken', 'hands', 'until', 'since', 'light']

    def print_instructions(self):
        print('Instructions: Learn to play alone')

    def game(self):

        self.print_instructions()
        solution = random.choice(self.word_list)
        life = 1
        win = False
        while life < 7:
            inputer = Inputer(self.word_list)
            word = inputer.get_word()
            checker = Checker(word, solution)
            checker.check_correct_letters()
            position_map = checker.check_missplaced_letters()
            self.draw(word, position_map, life)
            if self.is_game_won(position_map):
                win = True
                break
            life = life + 1

        if win:
            print('Congratulations, you win.')
        else:
            print('Better luck next time')

    def draw(self, word, position_map, life):
        formated_word = "|".join(list(word))
        formated_position_map = "|".join(position_map)
        print(f'Try {life} of 6')
        print(formated_word)
        print('-'*len(formated_word))
        print(formated_position_map)

    def is_game_won(self, position_map):
        if position_map == ['1']*5:
            return True
        else:
            return False

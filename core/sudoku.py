import numpy as np


class SudokuGame:
    """Class to create a sudoku game

    Attributes:
        game (array): numpy array with list of arrays

    """

    game = None
    divider_line = 37*'-'

    def __init__(self):
        self.game = np.array([
            [8, 4, None, None, None, None, None, None, 3],
            [None, 2, None, None, 7, 8, None, 5, 9],
            [None, None, None, 4, 2, None, None, None, None],
            [None, 6, None, None, None, None, 5, None, None],
            [None, 5, 7, None, 4, None, 1, 6, None],
            [None, None, 9, None, None, None, None, 4, None],
            [None, None, None, None, 5, 1, None, None, None],
            [1, 9, None, 8, 6, None, None, 7, None],
            [5, None, None, None, None, None, None, 8, 1]
        ])

    def print_divider_line(self):
        print(self.divider_line)

    @staticmethod
    def row_to_string(row):
        """Transform row to printable string

        Args:
            row (array): array with row elements

        Returns:
            string of chosen row.

        """

        string_row = '|'
        for element in row:
            if element:
                string_row = string_row + ' ' + str(element) + ' |'
            else:
                string_row = string_row + '   |'
        return string_row

    def print_game(self):
        self.print_divider_line()
        for row in self.game:
            print(self.row_to_string(row))
            self.print_divider_line()


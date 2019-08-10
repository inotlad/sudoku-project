import numpy as np


class SudokuGame:
    """Class to create a sudoku game

    Attributes:
        game (array): numpy array with list of arrays

    """

    game = None
    divider_line = 37*'-'
    element_options = [1,2,3,4,5,6,7,8,9]
    divider_block = 3

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

    def get_element_row_options(self, row_index):
        """Get all possible elements in a row.

        Args:
            row_index (int): index of the chosen row.

        Returns:
            Array with available elements in row.

        """

        row_elements = self.game[row_index][np.nonzero(self.game[row_index])]
        return np.setdiff1d(self.element_options, row_elements)

    def get_element_column_options(self, column_index):
        """Get all possible elements in a column.

        Args:
            column_index (int): index of the chosen column.

        Returns:
            Array with available elements in column.

        """

        column_elements = self.game[:,column_index][
            np.nonzero(self.game[:,column_index])
        ]
        return np.setdiff1d(self.element_options, column_elements)

    def get_element_block_options(self, row_index, column_index):
        """Get all possible elements in a block.

        Args:
            row_index (int): index row of chosen element.
            column_index (int): index column of chosen element.

        Returns:
            Array with available elements in a block.

        """

        block_row = row_index//self.divider_block
        block_column = column_index//self.divider_block
        block = self.game[
            block_row : block_row + self.divider_block,
            block_column : block_column + self.divider_block
        ]
        block_elements = block[np.nonzero(block)]
        return np.setdiff1d(self.element_options, block_elements)



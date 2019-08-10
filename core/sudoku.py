import numpy as np

class SudokuGame:

    game = None

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
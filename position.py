class Position:
    """
    Represents a position on a grid.

    :param row: The row number in the grid.
    :type row: int
    :param column: The column number in the grid.
    :type column: int
    """
    def __init__(self, row, column):
        self.row = row
        self.column = column

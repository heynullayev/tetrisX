import pygame
from colors import Colors


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        """
        Print the contents of the grid.

        :returns: None
        :rtype: None
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        """
        Check if a given row and column are inside the grid boundaries.

        :param row: The row index to check.
        :type row: int
        :param column: The column index to check.
        :type column: int
        :returns: Boolean indicating if the coordinates are inside the grid.
        :rtype: bool
        """
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def is_empty(self, row, column):
        """
        Check if a specific cell in the grid is empty.

        :param row: The row index to check.
        :type row: int
        :param column: The column index to check.
        :type column: int
        :returns: Boolean indicating if the cell is empty.
        :rtype: bool
        """
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        """
        Check if a row in the grid is completely filled.

        :param row: The row index to check.
        :type row: int
        :returns: Boolean indicating if the row is full.
        :rtype: bool
        """
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        """
        Clear the contents of a specific row in the grid.

        :param row: The row index to clear.
        :type row: int
        :returns: None
        :rtype: None
        """
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        """
        Move a row and the rows above it downwards by a specified number of rows.

        :param row: The row index to start the movement.
        :type row: int
        :param num_rows: The number of rows to move down.
        :type num_rows: int
        :returns: None
        :rtype: None
        """
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        """
        Clear all full rows in the grid and move rows down accordingly.

        :returns: The number of rows cleared.
        :rtype: int
        """
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        """
        Reset the grid by setting all cells to empty (0).

        :returns: None
        :rtype: None
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen):
        """
        Draw the grid on the screen.

        :param screen: Pygame screen object to draw on.
        :type screen: pygame.Surface
        :returns: None
        :rtype: None
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

from colors import Colors
import pygame
from position import Position


class Block:
    """
    Представляет блок.

    :param id: The identifier of the block.
    :type id: int
    """
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        """
        Перемещает блок на определенное количество строк и столбцов
        :param rows: The number of rows to move the block.
        :type rows: int
        :param columns: The number of columns to move the block.
        :type columns: int
        """
        self.row_offset += rows #обновление смещения по строкам
        self.column_offset += columns #по столбцам

    def get_cell_positions(self):
        """
        Получает позиции блока.

        :returns: List of Position objects representing cell positions.
        :rtype: list[Position]
        """
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        """
        Вращение блока
        :returns: None
        """
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        """
        Препятствывает последнему вращению

        :returns: None
        """
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        """
        Вырисовка блоков на экране

        :param screen: The pygame screen to draw on.
        :type screen: pygame.Surface
        :param offset_x: The x-coordinate offset for drawing.
        :type offset_x: int
        :param offset_y: The y-coordinate offset for drawing.
        :type offset_y: int
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
                                    offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

from grid import Grid
from blocks import *
import random
import pygame


class Game:
    """
       Основная механика игры

       :ivar grid: The grid object managing the game board.
       :vartype grid: Grid
       :ivar blocks: List of available blocks for the game.
       :vartype blocks: list
       :ivar current_block: The current falling block.
       :vartype current_block: Block
       :ivar next_block: The next block to fall after the current one.
       :vartype next_block: Block
       :ivar game_over: Flag indicating the game over status.
       :vartype game_over: bool
       :ivar score: The player's current score.
       :vartype score: int
       :ivar rotate_sound: Sound for block rotation.
       :vartype rotate_sound: pygame.mixer.Sound
       :ivar clear_sound: Sound for clearing rows.
       :vartype clear_sound: pygame.mixer.Sound
       """

    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")

        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)

    def update_score(self, lines_cleared, move_down_points):
        """
                Прибавление счета к игракам, после удаления нижней строки.

                :param lines_cleared: The number of lines cleared.
                :type lines_cleared: int
                :param move_down_points: Points earned through downward movement.
                :type move_down_points: int
                :returns: None
                :rtype: None
                """
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    def get_random_block(self):
        """
                Получение блока случайным образом

                :returns: A random block object.
                :rtype: Block
                """
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        """
                Перемещение блока влево, если он не находится у стены.

                :returns: None
                :rtype: None
                :raises: Exception if the block moves outside the grid.
                """
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        """
        Перемещение блока вправо, если он не находится у стены.

        :returns: None
        :rtype: None
        :raises: Exception if the block moves outside the grid.
        """
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        """
        Перемещение блока вниз, если он не находится у окончанчания игрового поля. И фиксация блока.

        :returns: None
        :rtype: None
        :raises: Exception if the block cannot fit inside or encounters issues during locking.
        """
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        """
        Фиксация текущего блока на месте, обновление счета играка, и удаление заполненных строк сетки

        :returns: None
        :rtype: None
        """
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    def reset(self):
        """
        Сброска игры к начальному исходу

        :returns: None
        :rtype: None
        """
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        """
        Проверка, помещается ли блок в границы сетки

        :returns: Boolean indicating if the block fits.
        :rtype: bool
        """
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        """
        Проверка возможности переворотов по часовой стрелки

        :returns: None
        :rtype: None
        :raises: Exception if the block encounters issues during rotation.
        """
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def block_inside(self):
        """
        Проверка нахождения текущего блока в границах сетки.

        :returns: Boolean indicating if the block is inside.
        :rtype: bool
        """
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        """
        Вырисовка элементов игры на экране.

        :param screen: Pygame screen object to draw on.
        :type screen: pygame.Surface
        :returns: None
        :rtype: None
        """
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)

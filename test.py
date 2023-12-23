import pytest
from unittest.mock import Mock, patch
from game import Game  

@pytest.fixture
def game():
    with patch('pygame.mixer.Sound'), patch('pygame.mixer.music'):
        return Game()

def test_update_score(game):
    game.update_score(1, 10)
    assert game.score == 110  

    game.update_score(2, 5)
    assert game.score == 415  

def test_get_random_block(game):
    initial_length = len(game.blocks)
    block = game.get_random_block()
    assert block is not None
    assert len(game.blocks) == initial_length - 1

def test_move_left(game):
    with patch.object(game.current_block, 'move'), patch.object(game, 'block_inside', return_value=True), patch.object(game, 'block_fits', return_value=True):
        game.move_left()
        game.current_block.move.assert_called_with(0, -1)

def test_move_right(game):
    with patch.object(game.current_block, 'move'), patch.object(game, 'block_inside', return_value=True), patch.object(game, 'block_fits', return_value=True):
        game.move_right()
        game.current_block.move.assert_called_with(0, 1)

def test_move_down(game):
    with patch.object(game.current_block, 'move'), patch.object(game, 'block_inside', return_value=True), patch.object(game, 'block_fits', return_value=True):
        game.move_down()
        game.current_block.move.assert_called_with(1, 0)

def test_block_fits(game):
    with patch.object(game.current_block, 'get_cell_positions', return_value=[]), patch.object(game.grid, 'is_empty', return_value=True):
        assert game.block_fits() is True

def test_block_inside(game):
    with patch.object(game.current_block, 'get_cell_positions', return_value=[]), patch.object(game.grid, 'is_inside', return_value=True):
        assert game.block_inside() is True

# Additional tests can be written for the draw method and other functionalities.

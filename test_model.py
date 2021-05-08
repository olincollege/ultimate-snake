"""
Unit tests for snake_model
"""

import pytest
import pygame
from snake_model import Board, Snake, Item

test_snake = Snake()
test_food = Item()
test_potion = Item()
test_speed_boost = Item()
test_board = Board(test_snake, test_food, test_potion, test_speed_boost)

def check_snake_property(_):
    """
    Check that the Board class has snake as a property.
    Returns:
        True if snake is a property of the Board class and False
        otherwise.
    """
    return isinstance(Board.snake, property)

def check_food_property(_):
    """
    Check that the Board class has food as a property.
    Returns:
        True if food is a property of the Board class and False
        otherwise.
    """
    return isinstance(Board.food, property)

def check_potion_property(_):
    """
    Check that the Board class has potion as a property.
    Returns:
        True if potion is a property of the Board class and False
        otherwise.
    """
    return isinstance(Board.potion, property)

def check_speed_boost_property(_):
    """
    Check that the Board class has speed_boost as a property.
    Returns:
        True if speed_boost is a property of the Board class and False
        otherwise.
    """
    return isinstance(Board.speed_boost, property)

def check_score_property(_):
    """
    Check that the Board class has score as a property.
    Returns:
        True if score is a property of the Board class and False
        otherwise.
    """
    return isinstance(Board.score, property)

@pytest.mark.parametrize("func", [check_snake_property, check_food_property,
                                  check_potion_property, check_speed_boost_property,
                                  check_score_property])

def test_properties(func):
    """
    Check that the board has correct properties.
    Args:
        func: A function that takes a string and returns a boolean, used to
            test the instance attributes of the refactored code.
    """
    assert func("")

item_eaten_cases = [
    #check that if the y and x coordinates are different for the snake head and item,
    #the function returns false
    ((50, 80), (60, 70), False),
    #check that for the snake head and the item, if the x coords are the same, but not the y,
    #the function returns false
    ((200, 30),(200, 50), False),
    #check that for the snake head and the item, if the y is the same, but not the x, the
    #function returns false
    ((200,50), (100, 50), False),
    #check that for the snake head and the item, if the x and y are the same, the
    #function returns true
    ((200,100), (200,100), True),
]

@pytest.mark.parametrize("head_coordinates, item_coordinates, eaten", item_eaten_cases)
def test_item_eaten(head_coordinates, item_coordinates, eaten):
    """
    Check that an item is only seen as eaten if the exact coordinates of the snake head
    overlap with the coordinates of the food item.
    
    Args:
        head_coordinates: A tuple containing the coordinates of the snake head.
        item_coordinates: A tuple containing the coordinates of the item.
        eaten: A boolian representing wither the item has been eaten or not.
    """
    test_board._snake._coordinates[0] = head_coordinates

    #check for the food items
    test_board._food._item_location = item_coordinates
    #check for the potion items
    test_board._potion._item_location = item_coordinates
    #check for the speed_boost items
    test_board._speed_boost._item_location = item_coordinates    
    
    assert (test_board.food_eaten() == eaten and test_board.potion_eaten() == eaten
        and test_board.speed_eaten() == eaten)


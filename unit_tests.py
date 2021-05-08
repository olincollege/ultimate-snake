"""
Unit tests for snake_model
"""

import pytest
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


def check_coordinates_property(_):
    """
    Check that the Snake class has coordinates as a property.
    Returns:
        True if coordinates is a property of the Snake class and False
        otherwise.
    """
    return isinstance(Snake.coordinates, property)

def check_direction_property(_):
    """
    Check that the Snake class has direction as a property.
    Returns:
        True if direction is a property of the Snake class and False
        otherwise.
    """
    return isinstance(Snake.direction, property)

def check_item_location_property(_):
    """
    Check that the Item class has item_location as a property.
    Returns:
        True if item_location is a property of the Item class and False
        otherwise.
    """
    return isinstance(Item.item_location, property)

@pytest.mark.parametrize("func", [check_snake_property, check_food_property,
                                  check_potion_property, check_speed_boost_property,
                                  check_score_property, check_coordinates_property,
                                  check_direction_property, check_item_location_property])

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
    ([50, 80], [60, 70], False),
    #check that for the snake head and the item, if the x coords are the same, but not the y,
    #the function returns false
    ([200, 30],[200, 50], False),
    #check that for the snake head and the item, if the y is the same, but not the x, the
    #function returns false
    ([200,50], [100, 50], False),
    #check that for the snake head and the item, if the x and y are the same, the
    #function returns true
    ([200,100], [200,100], True),
]

snake_collision_cases = [
    #check that if the head overlaps with the second snake segment, the function returns true
    ([[50, 80],[50,80]], True),
    #check that if the head overlaps with the third snake segment, the function returns true
    ([[50, 80],[30,50], [50,80]], True),
    #check that for the snake head and the body, if the x coords are the same, but not the y,
    #the function returns false
    ([[50, 80],[50,90]], False),
    #check that for the snake head and the body, if the y is the same, but not the x, the
    #function returns false
    ([[70, 80],[50,80]], False),
    #check that for the snake head and the body, if the x and y are different, the
    #function returns False
    ([[200,100], [300,50]], False),
]

wall_collision_cases = [
    #check that if the head x coordinate goes past the right wall, the function returns true.
    ([[571,500],[300,300]], True),
    #check that if the head x coordinate goes past the left wall, the function returns true.
    ([[29,500],[300,300]], True),
    #check that if the head y coordinate goes past the top wall, the function returns true.
    ([[40, 59],[300,300]], True),
    #check that if the head y coordinate goes past the bottom wall, the function returns true.
    ([[50, 571],[300,300]], True),
    #check that if the head x coordinate and y coordinate don't overlap with any wall, the function
    #returns false
    ([[300,300],[300,300]], False),
]

move_cases = [
    #check that the snake body updates correctly when going in the right direction
    ([30,0],[[30, 60],[30,90],[30, 120]], [[60,60],[30,60],[30,90]]),
    #check that the snake body updates correctly when going in the left direction
    ([-30,0],[[30, 60],[30,90],[30, 120]], [[0,60],[30,60],[30,90]]),
    #check that the snake body updates correctly when going in the up direction
    ([0,30],[[30, 60],[30,90],[30, 120]], [[30,90],[30,60],[30,90]]),
    #check that the snake body updates correctly when going in the down direction
    ([0,-30],[[30, 60],[30,90],[30, 120]], [[30,30],[30,60],[30,90]]),

]

add_segment_cases = [
    #check that the snake body updates correctly when going in the right direction
    ([30,0],[[30, 60],[30,90],[30, 120]], [[60,60],[30,60],[30,90],[30, 120]]),
    #check that the snake body updates correctly when going in the left direction
    ([-30,0],[[30, 60],[30,90],[30, 120]], [[0,60],[30,60],[30,90],[30, 120]]),
    #check that the snake body updates correctly when going in the up direction
    ([0,30],[[30, 60],[30,90],[30, 120]], [[30,90],[30,60],[30,90],[30, 120]]),
    #check that the snake body updates correctly when going in the down direction
    ([0,-30],[[30, 60],[30,90],[30, 120]], [[30,30],[30,60],[30,90],[30, 120]]),

]

@pytest.mark.parametrize("head_coordinates, item_coordinates, eaten", item_eaten_cases)
def test_item_eaten(head_coordinates, item_coordinates, eaten):
    """
    Check that an item is only seen as eaten if the exact coordinates of the snake head
    overlap with the coordinates of the food item.

    Args:
        head_coordinates: A list containing the coordinates of the snake head.
        item_coordinates: A list containing the coordinates of the item.
        eaten: A boolian representing whether the item has been eaten or not.
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

@pytest.mark.parametrize("snake_coordinates, collided",snake_collision_cases)
def test_snake_collision(snake_coordinates, collided):
    """
    Check that the snake is considered to have collided with its body only
    when its head coordinates are the same as any on of its body coordinates.

    Args:
        snake_coordinates: A list of lists containing the coordinates of each snake segment.
        collided: A boolian representing whether the snake has collided with itself or not.
    """
    test_board._snake._coordinates = snake_coordinates

    assert test_board.snake_collision()== collided

@pytest.mark.parametrize("body_coordinates, collided",wall_collision_cases)
def test_wall_collision(body_coordinates, collided):
    """
    Check that the snake is considered to have collided with the wall only
    when its head coordinates overlap with any of the wall coordinates.

    Args:
        body_coordinates: A list of lists containing the coordinates of each snake segment.
        collided: A boolian representing whether the snake has collided with the wall or not.
    """
    test_board._snake._coordinates = body_coordinates

    assert test_board.wall_collision()== collided

@pytest.mark.parametrize("direction, old_snake_coordinates, new_snake_coordinates",move_cases)
def test_move(direction, old_snake_coordinates, new_snake_coordinates):
    """
    Check that the snake's body updates its coordinates correctly when it moves in any direction.

    Args:
        direction: A list containing the direction that the snake should move
        old_snake_coordinates: A list of lists containing the coordinates of the old snake segments.
        new_snake_coordinates: A list of lists containing the coordinates of the new snake segments.
    """
    test_snake._coordinates = old_snake_coordinates
    test_snake.move(direction)

    assert test_snake._coordinates == new_snake_coordinates

@pytest.mark.parametrize("direction, old_snake, new_snake", add_segment_cases)
def test_add_snake_segment(direction, old_snake, new_snake):
    """
    Check that the snake's body updates its coordinates correctly when it moves in any direction.

    Args:
        direction: A list containing the direction that the snake should move
        old_snake: A list of lists containing the coordinates of the old snake segments.
        new_snake: A list of lists containing the coordinates of the new snake segments.
    """
    test_snake._coordinates = old_snake
    test_snake.add_snake_segment(direction)

    assert test_snake._coordinates == new_snake

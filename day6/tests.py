import pytest

from light_controller import LightController

@pytest.fixture
def controller():
    return LightController(size=10)

def test_parse_instruction(controller):
    instruction = 'turn on 0,0 through 9,9'
    action, start, end = controller.parse_instruction(instruction)
    assert action == 'on'
    assert start == (0, 0)
    assert end == (9, 9)

    instruction = 'turn off 5,5 through 7,7'
    action, start, end = controller.parse_instruction(instruction)
    assert action == 'off'
    assert start == (5, 5)
    assert end == (7, 7)

    instruction = 'toggle 0,0 through 9,0'
    action, start, end = controller.parse_instruction(instruction)
    assert action == 'toggle'
    assert start == (0, 0)
    assert end == (9, 0)

def test_apply_instruction_day_1_turn_on(controller):
    controller.apply_instruction_day_1('turn on 0,0 through 1,1')
    assert controller.grid[0][0] == 1
    assert controller.grid[1][1] == 1
    assert controller.grid[2][2] == 0

def test_apply_instruction_day_1_turn_off(controller):
    controller.apply_instruction_day_1('turn on 0,0 through 1,1')
    controller.apply_instruction_day_1('turn off 0,0 through 0,0')
    assert controller.grid[0][0] == 0
    assert controller.grid[1][1] == 1

def test_apply_instruction_day_1_toggle(controller):
    controller.apply_instruction_day_1('toggle 0,0 through 1,1')
    assert controller.grid[0][0] == True
    assert controller.grid[1][1] == True
    controller.apply_instruction_day_1('toggle 0,0 through 1,1')
    assert controller.grid[0][0] == False
    assert controller.grid[1][1] == False

def test_apply_instruction_day_2_turn_on(controller):
    controller.apply_instruction_day_2('turn on 0,0 through 1,1')
    assert controller.grid[0][0] == 1
    assert controller.grid[1][1] == 1
    controller.apply_instruction_day_2('turn on 0,0 through 1,1')
    assert controller.grid[0][0] == 2
    assert controller.grid[1][1] == 2

def test_apply_instruction_day_2_turn_off(controller):
    controller.apply_instruction_day_2('turn on 0,0 through 1,1')
    controller.apply_instruction_day_2('turn off 0,0 through 0,0')
    assert controller.grid[0][0] == 0
    assert controller.grid[1][1] == 1
    controller.apply_instruction_day_2('turn on 1,1 through 1,1')
    assert controller.grid[1][1] == 2
    controller.apply_instruction_day_2('turn off 1,1 through 1,1')
    assert controller.grid[1][1] == 1

def test_apply_instruction_day_2_toggle(controller):
    controller.apply_instruction_day_2('toggle 0,0 through 1,1')
    assert controller.grid[0][0] == 2
    assert controller.grid[1][1] == 2

def test_turn_off_grid(controller):
    controller.apply_instruction_day_1('turn on 0,0 through 9,9')
    assert controller.grid[0][0] == 1
    assert controller.grid[9][9] == 1
    controller.turn_off_grid()
    assert controller.grid[0][0] == 0
    assert controller.grid[9][9] == 0
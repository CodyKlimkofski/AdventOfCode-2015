import pytest
from elevator import Elevator

@pytest.fixture(scope="module")
def test_input():
    with open("day1/test-input.txt") as f:
        return f.read().strip()

@pytest.fixture
def elevator():
    return Elevator()

def test_process_instructions(elevator):
    assert elevator.process_instructions('(())') == 0
    assert elevator.process_instructions('()()') == 0
    assert elevator.process_instructions('(((') == 3
    assert elevator.process_instructions('(()(()(') == 3
    assert elevator.process_instructions('))(((((') == 3
    assert elevator.process_instructions('())') == -1
    assert elevator.process_instructions('))(') == -1
    assert elevator.process_instructions(')))') == -3
    assert elevator.process_instructions(')())())') == -3

def test_find_basement(elevator):
    assert elevator.find_basement(')') == 1
    assert elevator.find_basement('()())') == 5
    assert elevator.find_basement('(((') == -1
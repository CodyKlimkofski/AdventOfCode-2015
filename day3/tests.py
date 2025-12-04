import pytest 
from home_visitor import HomeVisitor

@pytest.fixture(scope="module")
def visitor():
    return HomeVisitor()

def test_initial_state(visitor):
    assert visitor.homes_visited == {(0, 0): 1}
    assert visitor.movers['Santa'] == (0, 0)
    assert visitor.movers['Robo'] == (0, 0)

def test_visit_day_1(visitor):
    visitor.visit_day_1('^')
    assert visitor.movers['Santa'] == (0, 1)
    assert visitor.homes_visited[(0, 1)] == 1

    visitor.visit_day_1('>')
    assert visitor.movers['Santa'] == (1, 1)
    assert visitor.homes_visited[(1, 1)] == 1

    visitor.visit_day_1('v')
    assert visitor.movers['Santa'] == (1, 0)
    assert visitor.homes_visited[(1, 0)] == 1

    visitor.visit_day_1('<')
    assert visitor.movers['Santa'] == (0, 0)
    assert visitor.homes_visited[(0, 0)] == 1

    visitor.visit_day_1('^')
    assert visitor.movers['Santa'] == (0, 1)
    assert visitor.homes_visited[(0, 1)] == 1

def test_visit_day_2(visitor):
    visitor.clear_visits()

    visitor.visit_day_2('^')
    assert visitor.movers['Santa'] == (0, 1)
    assert visitor.movers['Robo'] == (0, 0)
    assert visitor.homes_visited[(0, 1)] == 1

    visitor.visit_day_2('>')
    assert visitor.movers['Robo'] == (1, 0)
    assert visitor.movers['Santa'] == (0, 1)
    assert visitor.homes_visited[(1, 0)] == 1

    visitor.visit_day_2('v')
    assert visitor.movers['Santa'] == (0, 0)
    assert visitor.movers['Robo'] == (1, 0)
    assert visitor.homes_visited[(0, 0)] == 1

    visitor.visit_day_2('<')
    assert visitor.movers['Robo'] == (0, 0)
    assert visitor.movers['Santa'] == (0, 0)
    assert visitor.homes_visited[(0, 0)] == 1

    visitor.visit_day_2('^')
    assert visitor.movers['Santa'] == (0, 1)
    assert visitor.movers['Robo'] == (0, 0)
    assert visitor.homes_visited[(0, 1)] == 1
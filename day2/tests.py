import pytest
from wrapping_paper_estimator import WrappingPaperEstimator

@pytest.fixture(scope="module")
def estimator():
    return WrappingPaperEstimator()

def test_get_dimensions_from_text(estimator):
    assert estimator.get_dimensions_from_text("2x3x4") == (2, 3, 4)
    assert estimator.get_dimensions_from_text("1x1x10") == (1, 1, 10)

def test_get_side_sizes(estimator):
    assert estimator.get_side_sizes(2, 3, 4) == (6, 12, 8)
    assert estimator.get_side_sizes(1, 1, 10) == (1, 10, 10)

def test_get_lowest_side_size(estimator):
    assert estimator.get_lowest_side_size(2, 3, 4) == 6
    assert estimator.get_lowest_side_size(1, 1, 10) == 1

def test_get_side_perimeters(estimator):
    assert estimator.get_side_perimeters(2, 3, 4) == (10, 14, 12)
    assert estimator.get_side_perimeters(1, 1, 10) == (4, 22, 22)

def test_get_lowest_perimeter(estimator):
    assert estimator.get_lowest_perimeter(2, 3, 4) == 10
    assert estimator.get_lowest_perimeter(1, 1, 10) == 4

def test_get_cubic_volume(estimator):
    assert estimator.get_cubic_volume(2, 3, 4) == 24
    assert estimator.get_cubic_volume(1, 1, 10) == 10

def test_get_estimate_ribbon_length(estimator):
    assert estimator.estimate_ribbon_length("2x3x4") == 34
    assert estimator.estimate_ribbon_length("1x1x10") == 14

def test_estimate_wrapping_paper(estimator):
    assert estimator.estimate_wrapping_paper("2x3x4") == 58
    assert estimator.estimate_wrapping_paper("1x1x10") == 43
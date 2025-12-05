import pytest
from string_determiner import StringDeterminer

@pytest.fixture
def determiner():
    return StringDeterminer()

def test_is_nice_day_1(determiner):
    assert determiner.is_nice_day_1('ugknbfddgicrmopn') == True
    assert determiner.is_nice_day_1('aaa') == True
    assert determiner.is_nice_day_1('aeiouab') == False
    assert determiner.is_nice_day_1('hgfsdeu') == False
    assert determiner.is_nice_day_1('a') == False

def test_is_nice_day_2(determiner):
    assert determiner.is_nice_day_2('gjxyxgj') == True
    assert determiner.is_nice_day_2('xxyxx') == True
    assert determiner.is_nice_day_2('uurcxstgmygtbstg') == False
    assert determiner.is_nice_day_2('ieodomkazucvgmuy') == False

def test_has_repeated_pair(determiner):
    assert determiner._has_repeated_pair('xyxy') == True
    assert determiner._has_repeated_pair('aabcdefgaa') == True
    assert determiner._has_repeated_pair('aaa') == False
    assert determiner._has_repeated_pair('abcdefg') == False

def test_has_sandwiched_letter(determiner):
    assert determiner._has_sandwiched_letter('xyx') == True
    assert determiner._has_sandwiched_letter('abcdefeghi') == True
    assert determiner._has_sandwiched_letter('aaa') == True
    assert determiner._has_sandwiched_letter('abcd') == False
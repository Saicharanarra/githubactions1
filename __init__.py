# test_calculate_area_square.py

from main import calculate_area_square

def test_calculate_area_square():
    # Existing unit tests
    assert calculate_area_square(4) == 16
    assert calculate_area_square(0) == 0
    assert calculate_area_square(1.5) == 2.25

    # Failing unit test with changed input
    assert calculate_area_square(10) == 100  # Incorrect expected output

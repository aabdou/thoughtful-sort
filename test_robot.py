import pytest
from robot import sort

test_cases = [
    # (width, height, length, mass, expected)
    # STANDARD
    (10, 10, 10, 5,    "STANDARD"),  # normal package
    (10, 10, 10, 19.9, "STANDARD"),  # mass just below limit
    (99, 100, 100, 5,  "STANDARD"),  # volume just below limit (990000)
    (149, 149, 149, 5, "SPECIAL"),   # volume exceeds limit (3,307,949)

    # SPECIAL: heavy only
    (10, 10, 10, 20,   "SPECIAL"),   # exact mass limit
    (10, 10, 10, 25,   "SPECIAL"),   # mass above limit

    # SPECIAL: bulky by volume
    (100, 100, 100, 5, "SPECIAL"),   # exact volume limit (1000000)
    (200, 100, 100, 5, "SPECIAL"),   # volume above limit

    # SPECIAL: bulky by dimension
    (150, 10, 10, 5,   "SPECIAL"),   # width at limit
    (10, 150, 10, 5,   "SPECIAL"),   # height at limit
    (10, 10, 150, 5,   "SPECIAL"),   # length at limit

    # REJECTED: heavy and bulky
    (100, 100, 100, 20, "REJECTED"), # bulky by volume + heavy
    (150, 10, 10, 20,   "REJECTED"), # bulky by dimension + heavy
    (200, 200, 200, 50, "REJECTED"), # all limits exceeded
    (150, 1, 1, 20,     "REJECTED"), # exact limits

    # Edge cases
    (10, 10, 10, 0,    "STANDARD"),  # zero mass
]

@pytest.mark.parametrize("width, height, length, mass, expected", test_cases)
def test_sort(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected

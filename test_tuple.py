# test_tuple.py

import pytest

@pytest.mark.parametrize("input_x, expected", [
[2, 4],
[3, 6],
[5, 10]
])

def test_check_y_value(input_x, expected):
    from tuple_find_y import check_y_value
    answer = check_y_value(input_x)
    assert answer == expected

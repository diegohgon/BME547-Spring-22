# test_tuple.py

import pytest

@pytest.mark.parametrize("input_x1, input_x2, input_x3, input_y1, input_y2, expected_y3", [
[1, 2, 3, 1, 2, 3],
[3, 6, 9, 3, 6, 9],
[5, 10, 15, 5, 10, 15]
])

def test_check_y_value(input_x1, input_x2, input_x3, input_y1, input_y2, expected_y3):
    from tuple_find_y import check_y_value
    answer = check_y_value(input_x1, input_x2, input_x3, input_y1, input_y2)
    assert answer == expected_y3

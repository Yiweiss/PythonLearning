import main

def test_get_user_input():
    result = [1, 2, 6, 7, 4, 2]
    value = "1,2,6,7,4,2"
    assert (result == main.get_user_input(value))

def test_calc_average():
    result = 4.25
    assert (result == main.calc_average([2,4,5,6]))

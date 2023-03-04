# def test_one():
#     pass



# def test():
#     pass
# number = 2
#
# # def test4():
# #     assert number == 1, "oopsie"
#
# def test_is_int():
#     print("\n" + "the reuslts is ", isinstance(number, int))
#     assert isinstance(number, int)
#
#     """
#     int vs str/dictionary/tuple verification
#     """

import pytest
number = 0

# @pytest.mark.api
# @pytest.mark.positive
# def test_mark_pos():
#     assert number == 0
#
# @pytest.mark.positive
# @pytest.mark.skip
# def test_several_marks():
#     assert 0 == 0


# @pytest.mark.parametrize("actual, expected", [(0, number), ("a", number), (4, number)])
# def test_param(actual, expected):
#     assert actual == expected

# @pytest.mark.parametrize("value", [0, "number", "a", 4, 7])
# def test_param(value):
#     assert 7 == value


var = [10.000, 7, 10, 'aa', 'bb']

@pytest.mark.parametrize('value', var)
def test_param(value):
    assert 10 == value

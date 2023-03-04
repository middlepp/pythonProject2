import pytest
class TestMyFirst:
    """

    """

    my_number = 10
    @pytest.mark.positive
    def test_number_is_valid(self):
        """

        :return:
        """

        assert TestMyFirst.my_number == 10
    @pytest.mark.negativa
    def test_number_is_int(self):
        """

        :return:
        """

        assert (TestMyFirst.my_number + 2) is int


    @pytest.mark.parametrize("first, second, third", [(1, 1, 1), (8,7,6), (9,8,7)])
    def test_my_first(self, first, second, third):
        assert (first + second) == third
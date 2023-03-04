import time
class TestHomePage:

    def test_title(self):
        assert Base.Page.get_title(self) == H
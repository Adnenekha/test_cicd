from src.calculator import add, subtract

class TestCalculator:

    def test_addition(self):
        assert 4 == add(2, 2)

    def test_substraction(self):
        assert 0 == subtract(4, 4)

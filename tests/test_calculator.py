import sys
sys.path.insert(0, '../')
from src import calculator

class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_substraction(self):
        assert 0 == calculator.subtract(4, 4)

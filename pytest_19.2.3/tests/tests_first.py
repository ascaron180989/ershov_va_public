import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_division(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction(self):
        assert self.calc.subtraction(self, 20, 10) == 10

    def test_adding(self):
        assert self.calc.adding(self, 12, 18) == 30

import pytest
from equation_solver import Equation, Node, EquationSolver
def test_equation01():
    eq = EquationSolver("x = 0")
    assert eq.solve() == 0

def test_equation02():
    eq = EquationSolver("x = 1")
    assert eq.solve() == 1
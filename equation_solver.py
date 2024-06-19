import re

class Equation:
    def __init__(self, equation_str: str):
        self.equation_str = equation_str
        self.a, self.b, self.c = self.parse_equation(equation_str)
        self.validate()

    def parse_equation(self, equation_str: str):
        # Regex to extract coefficients from the equation
        match = re.match(r'(?P<a>[-+]?\d*)x\s*([-+])\s*(?P<b>\d+)\s*=\s*(?P<c>[-+]?\d+)', equation_str.replace(" ", ""))
        if not match:
            raise ValueError("La ecuación no tiene un formato válido.")
        
        a = int(match.group('a')) if match.group('a') not in ["", "+", "-"] else int(f"{match.group('a')}1")
        b = int(f"{match.group(2)}{match.group('b')}")
        c = int(match.group('c'))

        return a, b, c

    def validate(self):
        if self.a == 0:
            raise ValueError("El coeficiente 'a' no puede ser cero en una ecuación de primer grado.")
    
class EquationSolver:
    def solve(self, equation: Equation):
        return 0
from typing import Literal


class CalcOperations:
    def __init__(self, num1: float, num2: float, operator: Literal["a", "s", "m", "d"]):
        self.operations = {'a': ['+', self.addition],
                          's': ['-', self.subtraction],
                          'm': ['*', self.multiplication],
                          'd': ['/', self.division]}
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def string_expression(self, operator: Literal["a", "s", "m", "d"]):
        return f"{self.num1} {operator} {self.num2} = "

    def addition(self) -> float:
        return self.num1 + self.num2

    def subtraction(self) -> float:
        return self.num1 - self.num2

    def multiplication(self) -> float:
        return self.num1 * self.num2

    def division(self) -> float | str:
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return 'division by zero error'

    def math_expression(self):
        return self.string_expression(self.operations[self.operator][0]) + f"{self.operations[self.operator][1]()}"

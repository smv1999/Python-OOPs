# Class based Calculator program

class Calculator:
    def __init__(self, num1, num2):
        super().__init__()
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ArithmeticError:
            print("Error Occurred. Can't divide by zero")


calc = Calculator(23, 34)

print(calc.add())
print(calc.subtract())
print(calc.multiply())
print(calc.divide())

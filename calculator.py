class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y == 0:
            print("Cannot divide by zero.")
        else:
            self.result = x / y

# Example usage of the Calculator class
calc = Calculator()
calc.add(5, 3)
print("Result of addition:", calc.result)
calc.multiply(4, 2)
print("Result of multiplication:", calc.result)

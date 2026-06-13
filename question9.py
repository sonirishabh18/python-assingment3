class Calculator:

    def add(self, a, b):
        print("Addition =", a + b)

    def subtract(self, a, b):
        print("Subtraction =", a - b)

    def multiply(self, a, b):
        print("Multiplication =", a * b)

    def divide(self, a, b):
        print("Division =", a / b)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

c = Calculator()

c.add(num1, num2)
c.subtract(num1, num2)
c.multiply(num1, num2)
c.divide(num1, num2)

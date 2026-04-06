
class Addition:
    def addition(self, data1, data2):
        return data1 + data2
class Subtraction:
    def subtraction(self, data1, data2):
        return data1 - data2
class Multiplication:
    def multiplication(self, data1, data2):
        return data1 * data2
class Division:
    def division(self, data1, data2):
        if data2 != 0:
            return data1 / data2
        else:
            return "Cannot divide by zero"
class Calculator(Addition, Subtraction, Multiplication, Division):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
my_calculator = Calculator(10, 5)

print(f"Data 1: {my_calculator.data1}, Data 2: {my_calculator.data2}")
print(f"Addition: {my_calculator.addition(my_calculator.data1, my_calculator.data2)}")
print(f"Subtraction: {my_calculator.subtraction(my_calculator.data1, my_calculator.data2)}")
print(f"Multiplication: {my_calculator.multiplication(my_calculator.data1, my_calculator.data2)}")
print(f"Division: {my_calculator.division(my_calculator.data1, my_calculator.data2)}")

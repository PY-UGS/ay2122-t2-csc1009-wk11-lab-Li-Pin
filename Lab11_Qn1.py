class Calculator:
    def __init__(self, first, sec):
        self.first = first
        self.sec = sec

    # Add 2 numbers
    def adder(self):
        return self.first + self.sec

    # Subtract 2 numbers
    def subtractor(self):
        return self.first - self.sec

    # Multiply 2 numbers
    def multiplier(self):
        return self.first * self.sec

    # Divide 2 numbers
    def divider(self):
        return self.first / self.sec

    # Reset calculator to 0
    def clear(self):
        self.first = 0
        self.sec = 0


# Take in user input for 2 numbers
firstNum = float(input("Please enter the first number: "))
secondNum = float(input("Please enter the second number: "))

# Create an object and pass in values based on user input
cal = Calculator(firstNum, secondNum)

# Print all operations
print("Addition: ", cal.adder())
print("Subtraction: ", cal.subtractor())
print("Multiplication: ", cal.multiplier())
print("Division: ", cal.divider())
# Reset calculator
cal.clear()
# Value of first and second number is reset to 0
print(cal.first, cal.sec)

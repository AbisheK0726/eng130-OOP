import datetime

# Get the current time
# For the time into string
# Split the string into list by ":"
# Get the first element of the list
# Convert the string into integer
# Check the time and greet the user

def get_current_time():
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%H:%M:%S")
    return current_time

def greet_user(name):
    current_time = get_current_time()
    current_time = current_time.split(":")
    current_time = int(current_time[0])
    if current_time < 12:
        print(name, "Good Morning!")
    elif current_time < 16:
        print(name, "Good Afternoon!")
    elif current_time < 20:
        print(name, "Good Evening!")
    else:
        print(name, "Good Night!")

# greet_user("Abishek")

# ===========================================
# Task
# Create a simple calculator
# Create a class called Calculator
# Create a constructor
# Create methods for add, sub, mul, div

class Calculator:
    def __init__(self, number1, number2): # Self refers to the current instance of the class
        self.number1 = number1
        self.number2 = number2
    def add(self):
        return self.number1 + self.number2
    def sub(self):
        return self.number1 - self.number2
    def mul(self):
        return self.number1 * self.number2
    def div(self):
        return self.number1 / self.number2

# Ask the user what operation they want to perform
# Ask the user for two numbers
# Create an instance of the Calculator class
# Call the method based on the user input - add, sub, mul, div
# Print the result

def simple_calculator():
    opperation = input("Enter the operation you want to perform: ")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    calculator = Calculator(number1, number2)
    
    if opperation == "add":
        print(calculator.add())
    elif opperation == "sub":
        print(calculator.sub())
    elif opperation == "mul":
        print(calculator.mul())
    elif opperation == "div":
        print(calculator.div())
    else:
        print("Invalid operation")
        
# ========================================
# Ask the user for a number and a unit
# convert the number to meters if the unit is cm
# convert the number to centimeters if the unit is m
# print the result

def convert_cm_to_m():
    number = int(input("Enter the number: "))
    unit = input("Enter the unit: ")
    if unit == "cm":
        print(number / 100, "m")
    elif unit == "m":
        print(number * 100, "cm")
    else:
        print("Invalid unit")
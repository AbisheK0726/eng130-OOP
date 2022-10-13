import base_class as bc

# call all the functions in base_class in a child class

def simple_calculator():
    opperation = input("Enter the operation you want to perform: ")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    calculator = bc.Calculator(number1, number2)
    
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
            
simple_calculator()
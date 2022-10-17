# ===================================
# Q1
"""
method - function - 
declare a function called 
- 1 def user_name(): 
- 2 def user_name 
- 3 def user_name() 
- 4 def void user_name() 
- 5 user_name() 
- takes user name 
- displays welcome user name back to user in same line
"""

def user_name():
    name = input("Enter your name: ")
    print("Welcome", name)

# ===================================
# Q2
"""
control flow if elif else - for & while loops - how to iterate through a list of 5 items
"""

def loop_five():
    for i in range(5):
        print(i)
        
# ===================================
# Q3
"""
operators boolean expression "and" "or" etc andand && AND || which one is correct syntax

- and, is the correct syntax
- or is the correct syntax
- not is the correct syntax
"""

# ===================================
# Q4

"""
Data collections - dictionary - lists - tuple - indexing - 
print 3rd and 5th item from list 
- tuple - or dictionary 
- nested dict 
- list inside a dict 
- the list item from dict 
- which data type is mutable - immutable - 

Answer:
Tuples are immutable
Lists and dictionaries are mutable

"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}

print(my_list[2], my_list[4])
    
# ===================================
# Q5

"""
OOP 
- instance creation of a class 
- classes - 4 pillars - keywords super etc. - inheritance, polymorphism, encapsulation, abstraction
- bill = {"5": "4"} what type of data collections is this - Dictionary
- how to inherit a class 
- Super() 
- super().__init__ () - correct syntax
- super_init() 
replace existing code with correct syntax of super
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

# ===================================
# Q6
"""
string - any data type - how to add an item to to a list - tuple - dict etc
"""
my_list.append(11)
my_dict["eleven"] = 11
my_tuple = my_tuple + (11,) # You can't add to a tuple, you have to create a new tuple and then concatenate the two tuples together

# ===================================
# Q7
"""
problem solving skills with code examples - how to create an object of a class
"""
s = Student("Bob", 19, 12)
print(s.name)

# ===================================
# Q8
"""
calculation functions with args and return statements 
- return True or false based on the condition provided in the question 
- return "any" 
- DISPLAY true or false 
- create basic calculator functions without classes
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):    
    return a / b

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 5))

# ===================================
# Q9
"""
odd even number counter with range(1, 100)  odd & even numbers return only even number or otherwise 
- True or False 
- add the number if it is odd print if it is even 
- data collection
"""

def even_odd_counter():
    sum_of_odd = 0
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)
        else:
            sum_of_odd += i
    print("This is the sum of odd", sum_of_odd)
    

# ===================================
# Q10
"""
shopping_items = {"eggs": 1.85, "bread": 1.50, "peppers": 0.90} 
- print only values 
- print the total bill 
- print item with it's cost 
- create a function called food_bill and return above outcome
"""

def shopping_bill():
    shopping_items = {"eggs": 1.85, "bread": 1.50, "peppers": 0.90}
    print("Values:", shopping_items.values())
    
    total_bill = 0
    for item, cost in shopping_items.items():
        print(item, cost)
        total_bill += cost
        
    print("Total bill is", total_bill)
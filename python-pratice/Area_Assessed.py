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

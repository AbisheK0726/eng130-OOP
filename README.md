# Object Oriented Programming

## Contents

- [Introduction](#introduction)
- [4 Pillars of OOP](#4-pillars-of-oop)
- [Modules (Python)](#modules-python)
- [Method and Function](#method-and-function)

## Introduction

Object Oriented Programming (OOP) is a programming paradigm that uses objects and their interactions to design and program applications. OOP is a way of thinking about programming, based on real-world entities like objects, their attributes and methods.

### 4 Pillars of OOP

|Pillar|Description|
|:---|:---|
|Encapsulation|Encapsulation is the process of combining data and functions into a single unit called a class. Encapsulation is used to hide the values or state of a structured data object inside a class, preventing unauthorized parties' direct access to them.|
|Abstraction|Abstraction is the process of hiding the implementation details from the user, only the functionality will be provided to the user. In other words, the user will have the information on what the object does instead of how it does it.|
|Inheritance|Inheritance is the process of using details from a new class without modifying existing class. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).|
|Polymorphism|Polymorphism is the process of using a common interface for multiple forms (data types).|

### Modules (Python)

Modules are simply python files with a .py extension. The name of the module will be the name of the file.
Built-in modules are modules that are pre-installed with python. You can use them by importing them into your project.

**What are the benefits of using modules and built-in modules?**

1. Reusability of code - You don't have to write the same code again and again. You can just import the module and use it.
2. Code organization - You can organize your code into different files for better readability and organization.
3. Readability - You can import a module with a short name, making your code more readable.
4. Efficiency - You can import only the parts of a module that you need, instead of importing the whole module.

Example of built-in module:

```python
import math, random, datetime, sys

print(math.pi)
print(random.randint(1, 10))
print(datetime.date.today())
print(sys.version)
```

### Method and Function

A method is a function that is associated with an object. A method is called using the dot notation.

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

```python
def my_function():
  print("Hello from a function")

my_function()
```

### Classes

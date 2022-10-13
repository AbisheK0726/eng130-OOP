# Object Oriented Programming

## Contents

- [Introduction](#introduction)
- [4 Pillars of OOP](#4-pillars-of-oop)
- [Modules (Python)](#modules-python)
- [Method and Function](#method-and-function)

## Introduction

Object Oriented Programming (OOP) is a programming paradigm that uses objects and their interactions to design and program applications. OOP is a way of thinking about programming, based on real-world entities like objects, their attributes and methods.

### 4 Pillars of OOP
Look at oop_pillar.md

### Modules (Python)

Modules are simply python files with a .py extension. The name of the module will be the name of the file.
Built-in modules are modules that are pre-installed with python. You can use them by importing them into your project.
You can create your own modules by creating a python file with a .py extension.

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

"""
Python 3 - Twins(0 / 50 pts)
Report an issue
A twin of a word is a word written with the same letters (case insensitive) but not necessarily in the same order.
For example Silent is a twin of Listen.
The is_twin(a, b) function should return True if b is the twin of a and False otherwise. a and b are two strings and are not None.Write the body of the is_twin(a, b) function.
"""

# Create a function that takes 2 strings and returns True if they share all the same letters and False if they don't.
# The function should be case insensitive.

# Examples: 
# is_twin("yyoo", "yoyo") --> True
# is_twin("yyoo", "yoy") --> False

def is_twin(a, b):
    # write your code here
    if len(a) != len(b):
        print("The length of two words are not equal")
        return False
    a = a.lower()
    b = b.lower()
    for i in a:
        if i in b:
            b = b.replace(i, '', 1)
        else:
            return False
    return True

x = is_twin("Silent", "Listen")
y = is_twin("tracks", "Silent")

print(x)
print(y)
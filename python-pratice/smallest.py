"""
Python 3 - Intervals(0 / 120 pts)
Report an issue
Implement the find_smallest_interval(numbers) function which returns the smallest positive interval between two values of the numbers table.

For example given the table [1 6 4 8 2] the smallest interval is 1 (difference between 2 and 1)
Constraints:
numbers contains at least two numbers and a maximum of 100,000 entries.
The solutions which favor execution time on large size arrays will get the most points.
The difference between two elements will never exceed the size of an integer for your language
"""

# make function that takes a list of pos intergers
# 
# x = 6
# min = 99999999
# y = 1 - 6 = 5
# if y < min:
#   min = 5
# y = 1 -4 = 3
# if y < min:
#   min = y (3)

from msilib.schema import tables
import numbers


def find_smallest_interval(table):
    table.sort() # [1,2,4,6,8]
    
    min = table[1] - table[0] # min =  2 - 1 = 1. min - 1
    
    for i in range(1, len(table)-1): # loop through from 1 to 1 - the length of the table
        #print(i)
        check = table[i+1] - table[i]
        if check < min:
            min = check
    return min
        
print(find_smallest_interval([1,10,15,19,20]))

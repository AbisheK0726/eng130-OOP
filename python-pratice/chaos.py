import random as r

list_len = r.randint(1, 10) # create a list of random length
numbers = []

for i in range(list_len):
    numbers.append(r.randint(1, 1000)) # populate the list with random numbers


def find_largest(numbers_list):
    
    max = 0
    
    for i in numbers_list:
        if max < i:
            max = i
    return max


print(numbers)
print(find_largest(numbers))
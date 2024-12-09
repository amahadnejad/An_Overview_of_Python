"""
    For Loop
    To Run Use This In Terminal --> python for_loop.py
"""
# Example 1
fruits = ['apple', 'banana', 'cherry', 'kiwi']
for fruit in fruits:
    print(fruit)

# Example 2
numbers = range(1, 10)
for i in numbers:
    print(i)
# or
for i in range(1, 10):
    print(i)

for i in "banana":
    print(i)


fruits = ['apple', 'banana', 'cherry', 'kiwi']
for fruit in fruits:
    print(fruit)
    if fruit == 'cherry':
        break


fruits = ['apple', 'banana', 'cherry', 'kiwi']
for fruit in fruits:
    print(fruit)
    if fruit == 'cherry':
        continue

# Use range

# Print Number in 0, 15 range
for i in range(15):
    print(i)

# Print Number between two numbers
for i in range(3, 9):
    print(i)

for i in range(2, 16, 3):
    print(i)

# Using Else in Loop?
for i in range(10):
    print(i)
else:
    print('Done!')


# Another Example
for i in range(12):
    print(i)
    if i == 8:
        break
else:
    print('Done!')

for i in range(2):
    for j in range(4):
        print('->i=', i)
        print('-->j=', j)
        print('--->i*j=', i*j)
        print('-----')

# Another Example
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# Multiplication table (from 1 to 10) in Python

# To take input from the user
num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# End
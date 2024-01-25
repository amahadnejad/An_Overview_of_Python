"""
    Functions
    To Run Use This In Terminal --> python func.py

    A function is a block of code which only runs when it is called.
    You can pass data, known as parameters, into a function.
    A function can return data as a result.
"""

# Printing Hello Using Function
def hello():
    print("Hello From a Function!")

hello()

# Using Arguments
def hello(name):
    print(f"Hello {name}")

hello("Github")

# Default Argument
def country(name='Iran'):
    print(f'Im From {name}')

country()
country('Canada')
# country('France')

# Passing a List as an Argument
def my_list(food):
    for item in food:
        print(item)

food = ['pizza', 'Chicken', 'Burger', ]
my_list(food)

# using return
def x(num):
    return num * 2

print(x(5))
print(x(9))
print(x(8))
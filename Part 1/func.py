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
country('France')

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

# Average Function
def average(numbers):
    length = len(numbers)
    numbers_sum = 0
    for i in numbers:
        numbers_sum += i
    return numbers_sum/length

nums = [1, 2, 3, 4, 5]
print(average(nums))

print("-------")

# Getting Coffee Function
def get_coffee(money):
    coffee_cost = 3.50 # Assuming Coffee costs 3.50$
    if money >= 3.50:
        print("Okay! Boiling Coffee")
        print("Your Coffee is Ready!")
        change = money - coffee_cost
        print(f"Your Change: {change}")
    else:
        print("Sorry! You Don't have Enough Money For Coffee!")

budget = 3.5 # The Budget To Buy Coffee
get_coffee(budget)
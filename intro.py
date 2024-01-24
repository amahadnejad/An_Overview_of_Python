"""
    Intro
    To Run Use This In Terminal --> python intro.py
"""

# Write 'Hello World!' In Python
print('Hello World')

# Use Variables
x = 5
name = "John"
print(x)
print(name)

# Multiple Variables
a, b, c = "Orange", "Banana", "Kiwi"
print(a)
print(b)
print(c)
# or
print(a, b, c)

# One Value To Multiple Variables
a = b = c = "Orange"
print(a, b, c)

"""
Data Types:
    Python has the following data types built-in by default, in these categories:
        Text Type:	str
        Numeric Types:	int, float, complex
        Sequence Types:	list, tuple, range
        Mapping Type:	dict
        Set Types:	set, frozenset
        Boolean Type:	bool
        Binary Types:	bytes, bytearray
        None Type:	NoneType
"""

# Getting The Data Type
a = 5
print(type(a))

# operators -> +-*/
print(17+3)
print(15-8)
print(3*15)
print(9/3)

# If Else
a = 1280
b = 580

if b > a:
    print("b is Greater Than a")
else:
    print("a is Greater Than b")

print('--------')

# Use elif
a = 50
b = 879
c = 4300

if a > b and a > c:
    print("a is Greater Than b and c")
elif b > a and b > c:
    print("b is Greater Than a and c")
elif c > a and c > b:
    print("c is Greater Than a and b")

print('--------')

# While Loop
i = 1
while i < 6:
    print(i)
    i += 1

print('--------')

# use Break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


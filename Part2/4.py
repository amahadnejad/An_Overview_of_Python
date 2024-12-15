"""
Else In Comprehension
"""
# x = [ x for x in 'apple' if x in 'aeiov' else 'orange'] --> Error

x = [x if x in 'aeiov' else '*' for x in 'apple']
# print(x)


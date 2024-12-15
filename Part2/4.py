"""
Else In Comprehension
"""
# x = [ x for x in 'apple' if x in 'aeiov' else 'orange'] --> Error

x = [x if x in 'aeiov' else '*' for x in 'apple']
# print(x)


def foo(i):
    return i, i + .5

# for i in range(3):
#     for x in foo(i):
#         print(str(x))

# Whitespaces
a = [
    str(x)
    for i in range(3)
        for x in foo(i)]

print(a)




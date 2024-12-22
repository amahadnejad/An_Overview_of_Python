# a = [sorted(x) for x in [[2, 1], [4, 3], [0, 1]]]
# print(a)


def myfunc():
    [x*x for x in range(1, 10) if x == 2]


def ufunc():
    list(filter(lambda x: x == 2, map(lambda x: x*x, range(1, 10))))


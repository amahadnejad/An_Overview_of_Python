from timeit import timeit

# Comprehension Vs Iter

def iter():
    [x for x in range(100) if x > 10]


def loop():
    my_list = []
    for x in range(100):
        if x > 10:
            my_list.append(x)


def loop_fast():
    my_list = []
    for x in range(100):
        if x > 10:
            pass

print("Iter Func: ")
print(timeit('iter()', setup='from __main__ import iter'))
print("Loop Func: ")
print(timeit('loop()', setup='from __main__ import loop'))
print("Fast Loop Func: ")
print(timeit('loop_fast()', setup='from __main__ import loop_fast'))
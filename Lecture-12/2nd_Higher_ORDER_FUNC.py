def apply_function(func, value):
    return func(value)

def squre(x):
    return x * x

def increment(x):
    return x + 1

print(apply_function(squre, 5))
print(apply_function(increment, 5))
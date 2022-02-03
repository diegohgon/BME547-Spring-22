def my_function (a):
    if a<0:
        return "Cannot do this on a negative number."
    x = a + 5
    y = a - 5
    return x, y

first, second = my_function(1)
print(first)
print(second)

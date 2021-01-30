def my_func(x, y):
    try:
        num = x ** y
    except TypeError:
        return "Ошибка!"
    return num


print(my_func(2, 2))

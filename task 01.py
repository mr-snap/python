def my_f(s_1, s_2):
    try:
        sub = s_1 / s_2
    except ZeroDivisionError:
        return "Ошибка!"
    print(f"Результат {sub}")


my_f(s_1=int(input("s_1:")), s_2=int(input("s_2:")))

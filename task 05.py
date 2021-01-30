def my_func():
    res = 0
    while True:
        numbers = input("Введите набор чисел или 'q' для выхода: ").split()
        for i in numbers:
            try:
                if i == 'q':
                    print(f'Сумма равна {res}')
                    return
                else:
                    res += int(i)
            except ValueError:
                print("Введите набор чисел или 'q' для выхода: ")
        print(f'Сумма равна {res}')

print(my_func())
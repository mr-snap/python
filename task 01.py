from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Ваша зарплата: {time * rate + bonus}")
    except ValueError:
        print("Введите значения корректно")

salary()
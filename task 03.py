num_month = int(input('Введите число от 1 до 12:'))

month_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}

if num_month in month_dict:
    print(f'{num_month} - это {month_dict[num_month]}')
    if num_month == 1 or num_month == 2 or num_month == 12:
        print("Это зима")
    elif num_month == 3 or num_month == 4 or num_month == 5:
        print("Это весна")
    elif num_month == 6 or num_month == 7 or num_month == 8:
        print("Это лето")
    elif num_month == 9 or num_month == 10 or num_month == 11:
        print("Это осень")
    else:
        print("Нет времени года")
else:
    print("Месяц отсутствует")

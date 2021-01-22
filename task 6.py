while True:
    days = 1
    start = float(input('Стартовый результат:'))
    last = float(input("Финальный результат:"))
    if start <= 0 or last < 0:
        print("Результат должен быть больше 0")
    else:
        while start < last:
            start += start * 0.1
            days += 1
        print(f"Спортсмен добьётся резульатат за {days}")
        break

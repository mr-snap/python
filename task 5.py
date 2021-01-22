income = float(input("Выручка:"))
coasts = float(input("Убыток:"))
result = income - coasts
if result > 0:
    print(f'Ваша прибль составиляет {result}')
    print(f'Выша рентабильность составляет {result / income}')
    gdp = int(input('Сколько работает сотруднисков в ващей компании?'))
    print(f"На одного сотрудника Вашей компании приходится {result / gdp}")
elif result < 0:
    print(f'Ваша компания работает с убытком {-result}')
else:
    print("Ваша компания покрывает свои расходы без прибыли")

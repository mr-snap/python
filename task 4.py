n = int(input("Введите число:"))
m = n % 10
n = n // 10
while n > 0:
    if n % 10 > m:
        m = n % 10
    n = n // 10
print("Наибольшое цифра:", m)

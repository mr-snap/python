my_list = [5, 4, 2]
number = int(input("Введите новый элемент рейтинга:"))
i = 0
for n in my_list:
    if number <= n:
        i += 1
my_list.insert(i, number)
print(my_list)
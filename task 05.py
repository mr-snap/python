from functools import reduce

def my_list(el_1, el_2):
    return el_1 * el_2

uniq_list = [el for el in range(100, 1001, 2)]
print(f"Список\n{uniq_list}\n{reduce(my_list, uniq_list)}")
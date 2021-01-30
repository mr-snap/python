def my_func(num_1, nun_2, num_3):
    my_list = [num_1, nun_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return "Ошибка!"

print(my_func(2, 4, 8))
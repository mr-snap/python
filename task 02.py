def data(name, surname, birthday, city, email, phone):
    return f"Имя - {name}, Фамилия - {surname}, Год рождения - {birthday}, Город проживания - {city}, email - {email}, телеофн - {phone}"

print(data(name=input("Ваше имя: "), surname=input("Ваша фамилия: "), birthday=input("Ваш год рождения: "), city=input("Ваш город рождения: "), email=input("Ваш email: "), phone=input("Ваш номер телефона: ")))
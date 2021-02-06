my_file = open("text-1.txt", "w", encoding="utf-8")

line = " "
while line:
    line = input("Ввежите текст: ")
    my_file.write(f"{line}\n") if line != '' else my_file.close()
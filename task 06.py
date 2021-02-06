with open("text-6.txt", "r", encoding="utf-8") as txt_file:
    a = txt_file.readlines()
    for s in a:
        new_str = "".join((i if i in "1234567890" else " ") for i in s)
        new_str2 = [int(i) for i in new_str.split()]
        print(f"{s.split()[0]} {sum(new_str2)}")
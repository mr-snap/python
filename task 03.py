with open("text-3.txt", encoding="utf-8") as f:
    employeed_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f"Срелняя зарплата = {round(sum(employeed_dict.values()) / len(employeed_dict), 3)}\n"
    f"Работиники с зарплатой меньше 20к {[e[0] for e in employeed_dict.items() if e[1] < 20000]}")
with open("text-2.txt", encoding="utf-8") as f:
    line = f.readlines()
    for index, value in enumerate(line, 1):
        number = len(value.split())
        print(f"Строка {index} содержит {number} слов")
text = input("Введите тект:").split()

for i, word in enumerate(text, 1):
    print(f'{i}. {word[:10]}')
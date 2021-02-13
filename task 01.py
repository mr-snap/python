a = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 1, 2, 3]]
b = [[0, 1, 0, 1], [1, 3, 4, 7], [0, 1, 1, 2]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return "\n".join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return "\n".join(map(str, c))

matrix1 = Matrix(a)
matrix2 = Matrix(b)
print(f"Matrix 1\n{matrix1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix2}\n{'-' * 20}")
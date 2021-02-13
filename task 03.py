class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return "\n".join(["*" * rows for _ in range(self.nums // rows)]) + "\n" + "*" * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("Сумма ячеек: ")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Вычитание ячеек: ")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 else "Вычитание невозможно"

    def __mul__(self, other):
        print("Умножение ячеек: ")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Деление ячеек")
        return Cell(self.nums // other.nums)

cell1 = Cell(36)
cell2 = Cell(12)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 // cell2)
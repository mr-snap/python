class Stationery:
    def __init__(self, title="Предмет для рисования"):
        self.tittle = title

    def draw(self):
        print(f"Запуск отрисовки! {self.tittle}")


class Pen(Stationery):
    def draw(self):
        print(f"Рисуй с помощью {self.tittle} ручки!")

class Pencil(Stationery):
    def draw(self):
        print(f"Рисуй с помощью {self.tittle} карандаша!")

class Marker(Stationery):
    def draw(self):
        print(f"Рисуй с помощью {self.tittle} маркера!")


stat = Stationery()
stat.draw()
pen = Pen("синей")
pen.draw()
pencil = Pencil("красного")
pencil.draw()
marker = Marker("белого")
marker.draw()

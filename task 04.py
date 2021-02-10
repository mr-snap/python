class Car:
    ''' Автомобиль '''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Название машины: {self.name} цвета {self.color}, машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name}: Машина поехала")

    def stop(self):
        print(f"{self.name}: Машина остановилась")

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}')

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля: {self.speed}"

class TownCar(Car):
    """ Городской автомобиль """

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля: {self.speed}. Превышение скорость" if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"

class SportCar(Car):
    """ Спортивный автомобиль """

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля: {self.speed}. Превышение скорость" if self.speed > 180 else f"{self.name}: Скорость автомобиля {self.speed}"

class WorkCar(Car):
    """ Грузовой автомобиль """

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля: {self.speed}. Превышение скорость" if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"

class PoliceCar(Car):
    """ Полицейский автомобиль """

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar("Рено", "Чёрный", 60)
town_car.go()
print(town_car.show_speed())
town_car.turn(0)
town_car.stop()
print()

sport_car = SportCar("Ягуар", "Красный", 181)
sport_car.go()
print(sport_car.show_speed())
sport_car.turn(0)
sport_car.stop()
print()

work_car = WorkCar("Камаз", "Синий", 39)
work_car.go()
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print()

police_car = PoliceCar("Ниссан", "Белый", 59)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

print(f"\nМашина {town_car.name} (цвет {town_car.color})")
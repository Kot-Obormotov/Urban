#module_6_3 Множественное наследование

from random import randint

class Animal:
    """
    Animal - класс описывающий животных.
    Класс обладает следующими атрибутами:
    live - живое или нет
    sound - звук (изначально отсутствует)
    _DEGREE_OF_DANGER - степень опасности существа
    """
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    """
    Объект этого класса обладает следующими атрибутами:
    _cords = [0, 0, 0] - координаты в пространстве
    speed = ... - скорость передвижения существа (определяется при создании объекта)
    """
    def __init__(self, speed: int, _cords = [0, 0, 0]):
        self._cords = _cords
        self.speed = speed

    def move(self, dx: int, dy: int, dz: int):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0" )

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] -= int(abs(dz) * self.speed/2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

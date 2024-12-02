#module_6_1 Зачем нужно наследование

class Animal:
    """
    Класс Animal с параметрами
        name   - имя
        alive  - живо ли
        fed    - голодное ли
    и методом eat с параметром food - съело животное еду или нет
    """
    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    """
    Класс Plant с параметрами
        name - имя
        edible - съедобна еда или нет
    """
    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible

#несколько дочерних классов
class Mammal(Animal):
    pass

class Predator (Animal):
    pass

class Flower(Plant):
    pass

#класс Fruit идёт с переопределением, чтобы показать - фрукты съедобны
class Fruit (Plant):
    def __init__(self, name, edible=True):
        self.name = name
        self.edible = edible


# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(p2.name, p2.edible)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
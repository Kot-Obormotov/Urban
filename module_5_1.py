#module_5_1 Атрибуты и методы объекта

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floors = self.number_of_floors
        if new_floor <= floors and new_floor <= 0:
            for i in range(new_floor):
                print(i+1)
        else:
            print('Такого этажа не существует')

h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h1.go_to(0)

h2.go_to(18)
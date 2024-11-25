#module_5_1 Атрибуты и методы объекта

#Объявим класс House с атрибутами name и number_of_floors
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

#Определим модуль для "подъёма на этаж"
    def go_to(self, new_floor):
        floors = self.number_of_floors                  #вспомогательная переменная для хранения кол-ва этажей. Можно и без неё
        if new_floor <= floors and new_floor <= 0:
            for i in range(new_floor):
                print(i+1)                              #если есть подходящий этаж - "поднимаемся" на него
        else:
            print('Такого этажа не существует')

#тестовые дома
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

#тестовые подъёмы
h1.go_to(5)
h1.go_to(0)
h2.go_to(18)

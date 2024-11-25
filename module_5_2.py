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

#Дополним класс House методами для вывода количества этажей...
    def __len__(self):
        return self.number_of_floors

#...и вывода имени дома
    def __str__(self):
        str = f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
        return str


#тестовые дома
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('ЖК Горский', 18)
h4 = House('Домик в деревне', 2)

#тестовые вызовы
# __str__
print(h1)
print(h2)
print(h3)
print(h4)

# __len__
print(len(h1))
print(len(h2))
print(len(h3))
print(len(h4))
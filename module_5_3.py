#module_5_3 Перегрузка операторов

#Объявим класс House с атрибутами name и number_of_floors
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

#Дополним класс House методами для вывода количества этажей...
    def __len__(self):
        return self.number_of_floors

#...и вывода имени дома
    def __str__(self):
        str = f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
        return str

#перегрузим несколько операторов
    def __eq__(self, other):
        if isinstance(other,House):
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False

    def __lt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors < other.number_of_floors:
                return True
            else:
                return False

    def __le__(self, other):
        if isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors:
                return True
            else:
                return False

    def __gt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors > other.number_of_floors:
                return True
            else:
                return False

    def __ge__(self, other):
        if isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors:
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(other, House):
            if self.number_of_floors != other.number_of_floors:
                return True
            else:
                return False

#определим метод для увеличения этажей дома
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

#переопределим метод __add__
    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


#Тестовые дома
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#тестовые вызовы из условия задачи
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
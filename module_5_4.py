#module_5_4 Различие атрибутов класса и экземпляра

#Объявим класс House с атрибутами name и number_of_floors
class House:
    #список для фиксации объектов класса
    houses_history = []

    # переопределим обработку метода __new__ для записи данных об объектах класса
    def __new__(cls, *args, **kwargs):
        new_house = object.__new__(cls)
        cls.houses_history.append(args[0])
        return new_house

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


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



#тестовые дома из условия задачи
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
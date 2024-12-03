#module_6_2 Доступ к свойствам родителя. Переопределение свойств

class Vehicle:
    """
    Класс Vehicle
        Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания.
        Атрибуты объектов класса:
            owner(str) - владелец транспорта. (владелец может меняться)
            __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
            __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
            __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
    """
    #Задание списка возможных цветов авто
    __COLOR_VARIANTS = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    #набор модулей для получения информации
    def get_model(self):
        return f'Модель: {self.__model}\n'

    def get_horsepower(self):
        return f'Мощность: {self.__engine_power}\n'

    def get_color(self):
        return f'Цвет: {self.__color}\n'

    #Общий модуль вывода информации. Почему-то позиции после первой выводит с отступом в 1 пробел, возможно из-за версии pycharm
    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    """
    Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
    Атрибут __PASSENGERS_LIMIT = X (в седан может поместиться только X пассажиров)
    """
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства автомобиля
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

#Проверяем что поменялось
vehicle1.print_info()



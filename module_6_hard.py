#module_6_hard Дополнительное практическое задание по модулю "Наследование классов"

import math

class Figure:
    """
    Атрибут класса: sides_count = 0 - количество сторон
    Атрибуты(инкапсулированные):
        __sides(список сторон (целые числа)), __color(список цветов в формате RGB)

    Атрибуты(публичные): filled(закрашенный, bool)
    """
    sides_count = 0

    def __init__(self, __color: tuple[int, int, int], filled = False, *__sides):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        #форматируем вывод согласно ТЗ
        return  list(self.__color)

    @staticmethod   #Декораторы - крутая штука. Но пришлось искать информацию отдельно - нет урока по их использованию (есть про счётчик вызова функции, но там нет упоминания потому что рано наверное)
    def __is_valid_color(r, g, b):
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_values and valid_types

    #проверяем цвет и заливаем
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = True

    @staticmethod
    def __is_valid_sides(*sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    #проверяем стороны и фиксируем количество
    def get_sides(self):
        # форматируем вывод согласно ТЗ
        return list(self.__sides)

    #подсчёт периметра
    def __len__(self):
        return sum(self.__sides)

    #проверяем количество сторон относительно типа фигуры и фиксируем их значения
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            valid_sides = []
            for side in new_sides:
                if self.__is_valid_sides(side):
                    valid_sides.append(side)
            self.__sides = valid_sides

class Circle(Figure):
    """
    Атрибут __radius рассчитывается из длины окружности, она же единственная сторона
    """
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], length):
        super().__init__(color, length)
        self.__radius = length / (2 * math.pi)

    #вычисление площади круга
    def get_square(self):
        return self.__radius ** 2 / (4 * math.pi)

class Triangle(Figure):
    """
    У треугольника три стороны
    Остальное как и у всех фигур
    """
    sides_count = 3

    def __init__(self, color: tuple[int, int, int], *sides):
        super().__init__(color, *sides)

    #площадь треугольника по формуле Герона
    def get_square(self):
        p = len(self)/2
        sides = self.get_sides()
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

class Cube(Figure):
    """
    Куб имеет 12 одинаковых сторон
    """
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], side):
        # Почему-то pycharm выводит массив из 11 элементов-сторон если поставить 12. Магия
        cube_sides = [side] * 13
        super().__init__(color, *cube_sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3

#Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
#module_8_1 "Try и Except"

"""
add_everything_up, будет складывать числа(int, float) и строки(str)
"""


def add_everything_up(a, b):
    try:
        #пробуем сложить и округлить числа (костыль - версия pycharm выдаёт сумму в третьем тесте 130.45600000000002)
        str_ = a+b
    except TypeError:
        #если нет возможности, то переводим в строковое и соединяем
        str_ = str(a)+str(b)
    return str_

#Тест
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

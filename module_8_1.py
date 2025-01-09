#module_8_1 "Try и Except"

def add_everything_up(a, b):
    try:
        str_ = round(a+b, 3)
    except TypeError:
        str_ = str(a)+str(b)
    return str_

#Тест
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
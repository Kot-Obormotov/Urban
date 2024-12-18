#module_3_3 Распаковка позиционных параметров

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#1 Функция с параметрами по умолчанию:
print_params()                      #вывод значений по умолчанию
print_params(23,'bla')        #вывод с неполной задачей аргументов
print_params(b = 25)                #замена аргумента 'b' с изменением типа данных
print_params(c = [1,2,3])           #замена аргумента 'с' с изменением типа данных

#2 Распаковка параметров:
values_list = [False, 'argument', 1.5]      #список по условию задания
values_dict ={'a': 1, 'b': 2, 'c': 'kwargument'}  #словарь по условию задания

print_params(*values_list)
print_params(**values_dict)

#3 Распаковка + отдельные параметры:

values_list_2 = ['fizz', 2.666666]
print_params(*values_list_2, 42)        #передача параметров из списка в качестве аргументов функции (в данном случае первых двух)
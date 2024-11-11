#module_3_hard Дополнительное практическое задание по модулю 3

#структура из задания
data_structure = [
  [1, 2, 3],                                #6
  {'a': 4, 'b': 5},                         #11
  (6, {'cube': 7, 'drum': 8}),              #6 + 23
  "Hello",                                  #5
  ((), [{(2, 'Urban', ('Urban2', 35))}])    #48
]

def summation(data_structure):
    sum = 0                                                             #внутренняя переменная для хранения суммы
    for i in data_structure:
        if isinstance(i, int):                                              #определяем возможный тип данных и суммируем значение числа либо длину строки
            sum += i
        elif isinstance(i, str):
            sum += len(i)
        elif isinstance(i, list):                                           #обращение к элементу списка и обработка его по одному из сценариев выше
            sum += summation(i)
        elif isinstance(i, dict):
            sum = sum + summation(i.keys()) + summation(i.values())     #обращение к ключу словаря или к значению и обработка по одному из сценариев выше
        elif isinstance(i, (tuple, set)):
            sum += summation(list(i))                                   #переформатирование множества или кортежа в список и рекурсивная обработка списка по сценарию выше
    return sum

print(summation(data_structure))

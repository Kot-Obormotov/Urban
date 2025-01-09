#module_8_2 "Сложные моменты и исключения в стеке вызовов функции"

"""
Функция personal_sum(numbers):

    Должна принимать коллекцию numbers.
    Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
    Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
    В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во некорректных данных.

Функция calculate_average(numbers)

Среднее арифметическое - сумма всех данных делённая на их количество.

    Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
    Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
    Так как коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
    Также в numbers может быть записана не коллекция, а другие типы данных, например числа. Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None.
"""

def personal_sum(numbers):
    # контейнеры для данных
    result  = 0
    incorrect_data = 0
    # перебор коллекции с подсчётом суммы входящих чисел
    for num in numbers:
        try:
            result += num
        except TypeError:
            # если пытаемся прибавить строку - ошибка
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {num, type(num)}')
    return [result, incorrect_data]

# можно было не заморачиваться с функцией, а оставить перебор внутри calculate_average,
# но так выглядит чище
def count_numbers(numbers):
    count = 0
    for num in numbers:
        if type(num) is not str:
            count += 1
    return count

def calculate_average(numbers):
    try:
        #подсчёт среднего с использованием функций выше
        result = personal_sum(numbers)[0]/count_numbers(numbers)
        return result
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')

#Тесты
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
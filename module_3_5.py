# #module_3_5 Рекурсия

#Рекурсивная функция для перемножения значимых цифр в int числе
def get_multiplied_digits(number):
    str_number = str(number)                                        #для перебора цифр в числе переведём в строку
    first = int(str_number[0])                                      #возьмём "первую" цифру
    if len(str_number) > 1 and int(str_number[1:]) != 0:            #если мы не добрались до последнего числа и последнее число не ноль продолжаем перемножать
        first *= get_multiplied_digits(int(str_number[1:]))         #фиксируем в переменной
    return first

#Тесты
result = get_multiplied_digits(40203)
print(result)

result1 = get_multiplied_digits(50005)
print(result1)

result2 = get_multiplied_digits(3330000000000)
print(result2)

result3 = get_multiplied_digits(12345)
print(result3)
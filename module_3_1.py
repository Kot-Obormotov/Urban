#module_3_1 Пространство имён

#переменная счётчик
calls = 0

# функция подсчёта вызовов других функций
def count_calls(fu):
    global calls
    calls = calls + 1
    return calls

# функция для сбора информации о введённой строке
def string_info(string):
    count_calls(string_info)            #вызов счётчика
    length = len(str(string))
    cap = str(string).upper()
    low = str(string).casefold()
    set_string_info = (length, cap, low)
    return set_string_info

# функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls(is_contains)            #вызов счётчика
    flag = True
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).casefold() == str(string).casefold():
            flag = True
        else:
            flag = False
    return flag

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(string_info('А роза упала на лапу Азора'))
print(string_info(''))
print(is_contains('Music', ['Rock', 'Funk', 'Disco'])) # No matches
print(is_contains('Poland', ['Germany', 'PoLaNd', 'pOLAND'])) # Poland = pOLAND = PoLaNd

print(calls)
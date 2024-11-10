#module_3_4 Произвольное число параметров

def single_root_words (root_word, *other_words):
    '''
    Функция для определения однокоренных слов из списка
    :param root_word:
    :param other_words:
    :return:
    '''
    same_words = []                                         #пустой список для фиксации результата
    for i in other_words:                                   #проход по списку
        if i.lower().find(root_word.lower()) != -1:         #поиск основного слова в слове из списка; всё в нижнем регистре
            same_words.append(i)                            #если есть - добавить
        elif root_word.upper().find(i.upper()) != -1:       #поиск слова из списка в основном слове; всё в верхнем регистре
            same_words.append(i)                            #если есть - добавить
    return same_words

#Тестовые значение и вывод результатов
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)

result3 = single_root_words('Pomegranate', 'Granate', 'gRAN', 'pom', 'Nate', 'Grenade', 'migrane')
print(result3)
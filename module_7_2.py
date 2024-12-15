#module_7_2 "Позиционирование в файле"

#функция перебирает позиции списков *strings и фиксирует их в файл file_name
# выводит позицию, байт начала строки файла (курсор) куда ведёт запись и содержание элемента списка
def custom_write(file_name: str, *strings: list):
    strings_positions = {}
    with open(file_name, 'w', encoding='UTF-8') as file:
        for string in strings:
            str_num = 0
            for line in string:
                strings_positions[str_num, file.tell()] = line
                file.write(f'{line}\n')
                str_num += 1
    return strings_positions

#Тест
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
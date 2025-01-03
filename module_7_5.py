#module_7_5 "Файлы в операционной системе"

import os
from datetime import datetime

"""
Создайте новый проект или продолжите работу в текущем проекте.
    Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
    Примените os.path.join для формирования полного пути к файлам.
    Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
    Используйте os.path.getsize для получения размера файла.
    Используйте os.path.dirname для получения родительской директории файла.
"""

print() #Просто разделение, чтобы было видно следующие данные
os.chdir(os.getcwd()) #фиксируем директорию, чтобы не работать со всей файловой системой

#формируем списки файлов, директорий и корней файлов потому что так в тз к задаче
for root, dirs, files in os.walk(os.getcwd()):
    files = [f for f in os.listdir() if os.path.isfile(f)]
    dirs = [d for d in os.listdir() if os.path.isdir(d)]
    root = [file for file in files if os.path.abspath(file)]

#можно было коррелировать данные между root, files и dirs,
#но в задаче стоит работа с модулем os так что делаем проход только по именам файлов
for file in files:
    #определяем абсолютный путь до файла (в задаче не сказано, что нужна относительная)
    filepath = os.path.abspath(file)
    # определяем время создания файла и форматируем его в удобоваримый формат
    filetime = datetime.fromtimestamp(os.path.getatime(file)).strftime("%d.%m.%Y %H:%M")
    # определяем время изменения файла и форматируем его в удобоваримый формат
    formatted_time = datetime.fromtimestamp(os.path.getmtime(file)).strftime("%d.%m.%Y %H:%M")
    # определяем размер файла в байтах
    filesize = os.path.getsize(file)
    # #определяем абсолютный путь родительской директории файла (в задаче не сказано, что нужна относительная)
    parent_dir = os.path.abspath(os.path.join(filepath, os.pardir))
    print(
        f'Обнаружен файл: {file}, '
        f'Путь: {filepath}, ','\n',
        f'Размер: {filesize} байт, '
        f'Время создания: {filetime}, '
        f'Время изменения: {formatted_time}, '
        f'Родительская директория: {parent_dir}')

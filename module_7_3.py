#module_7_3 "Оператор "with"

class WordsFinder:
    """
        Атрибут класса file_names - список имён файлов, определяемый при создании. Т.е. *args
    """
    file_names = []

    def __init__(self, *file_names):
        for file_name in file_names:
            with open(file_name, 'r'):
                self.file_names.append(file_name)

    #Пройдём по каждому файлу и создадим словари со словами из этих файлов
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='UTF-8') as file:
                text = file.read()
                all_words[file_name] = text.split()
        return all_words

    #поиск заданного слова в тексте каждого файла
    #можно было сделать через get_all_words(), но нет времени)
    def find(self, word: str):
        found = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='UTF-8') as file:
                text = file.read().lower().split()
                for words in text:
                    if word.lower() in text:
                        found[file_name] = text.index(words.lower()) + 1 #потому что индекс идёт от 0
                    else:
                        found[file_name] = 'No such word'
        return found

    #подсчёт появления конкретного слова в тексте каждого файла
    def count(self, word: str):
        _count = 0
        _count_dict = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='UTF-8') as file:
                text = file.read().lower().split()
                for words in text:
                    if words == word.lower():
                        _count += 1
                _count_dict[file_name] = _count
        return _count_dict

#Тест
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
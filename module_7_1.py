#module_7_1 "Режимы открытия файлов"

from pprint import pprint, pformat

class Shop:
    """
    Инкапсулированный атрибут __file_name = 'products.txt'.
    Метод get_products(self), который считывает всю информацию из файла __file_name,
        закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
    Метод add(self, *products), который принимает неограниченное количество объектов класса
        Product. Добавляет в файл __file_name каждый продукт из products, если его ещё нет
        в файле (по названию). Если такой продукт уже есть, то не добавляет и выводит строку
        'Продукт <название> уже есть в магазине'.
    """
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        text = file.read()
        file.close()
        return text

    def add(self, *products):
        #из-за оператора with можно не закрывать файл
        with open(self.__file_name, 'a') as file:
            products_list = self.get_products()
            #перебираем продукты по имени и смотрим, есть ли они в перечне
            #если нет - записываем
            for product in products:
                if product.name not in products_list:
                    file.write(f'{product.__str__()}\n')
                else:
                    print(f'Продукт {product.name} уже есть в магазине')

class Product(Shop):
    """
    Атрибут name - название продукта (строка).
    Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
    Атрибут category - категория товара (строка).
    Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
    """
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

#Тесты
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())
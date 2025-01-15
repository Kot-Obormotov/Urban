#module_8_3 Создание исключений

class Car:
    """
    Атрибут объекта model - название автомобиля (строка).
    Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
    Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
        Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    Атрибут __numbers - номера автомобиля (строка).
    Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
        Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    """
    def __init__(self, model: str, __vin: int, __numbers: str):
        if self.__is_valid_model(model):
            self.model = model
        if self.__is_valid_vin(__vin):
            self.__vin = __vin
        if self.__is_valid_numbers(__numbers):
            self.__numbers = __numbers

    @staticmethod
    def __is_valid_model(car_model):
        """
    Выбрасывает исключение IncorrectCarName с сообщением 'Некорректный тип данных для модели авто',
        если передана не строка.
    Возвращает True, если исключения не были выброшены.
    """
        if not isinstance(car_model, str):
            raise IncorrectVinNumber('Некорректный тип данных для модели авто')
        return True

    @staticmethod
    def __is_valid_vin(vin_number):
        """
    Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
        если передано не целое число.
    Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
        если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
    Возвращает True, если исключения не были выброшены.
    """
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    @staticmethod
    def __is_valid_numbers(numbers):
        """
    Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
        если передана не строка.
    Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
        переданная строка должна состоять ровно из 6 символов.
    Возвращает True, если исключения не были выброшены.
    """
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectVinNumber('Неверная длина номера')
        return True

class IncorrectCarName(Exception):
    """
    Обладает атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения
    """
    def __init__(self, message):
        self.message = message

class IncorrectVinNumber(Exception):
    """
    Обладает атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения
    """
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    """
    Обладает атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения
    """
    def __init__(self, message):
        self.message = message

#Тесты
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectCarName as exc:
    print(exc.message)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectCarName as exc:
    print(exc.message)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectCarName as exc:
    print(exc.message)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

try:
    fourth = Car(123456, '2020202', 15.6)
except IncorrectCarName as exc:
    print(exc.message)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{fourth.model} успешно создан')



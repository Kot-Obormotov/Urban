#module_4_1 Модули и пакеты
from fake_math import divide as fake_divide     #импорт неправильной математики
from true_math import divide as true_divide     #импорт правильной математики

#тесты
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)
# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:

# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Количество положительных элементов в первой половине:

import random

count= int(input("Введите количество элементов "))
min_val= int(input("От какого числа "))
max_val= int(input("До какого числа "))

numbers=[random.randint(min_val, max_val) for _ in range(count)]

# Сразу считаем нужные значения
count = len(numbers)
min_num = min(numbers)
pos_in_half = sum(1 for num in numbers[:count//2] if num > 0)
with open('numbers.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(map(str, numbers)))

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f"""Исходные данные: {' '.join(map(str, numbers))}
    Количество элементов: {count}
    Минимальный элемент: {min_num}
    Количество положительных элементов в первой половине: {pos_in_half}""")

print("Готово! Результат в result.txt")

    







# 
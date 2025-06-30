# В двумерном списке найти сумму элементов первых двух строк.

import random

matrix = (lambda rows, cols: [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)])(3, 2)
sum_two_rows = (lambda m: sum(m[0]) + sum(m[1]))(matrix)

print("Список:", *matrix, )
print("Сумма первых двух строк:", sum_two_rows)
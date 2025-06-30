#В последовательности на n целых чисел умножить все элементы на последний
#минимальный элемент.


import random
numbers = [random.randint(1, 20)for i in range(5)]
print(numbers)
result=map(lambda x: x * min(numbers), numbers)
print(list(result))



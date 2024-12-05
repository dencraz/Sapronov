# Дан список A ненулевых целых чисел размера 10. Вывести значение первого из тех
# его элементов AK, которые удовлетворяют неравенству AK < A10. Если таких
# элементов нет, то вывести 0.
# Инициализируем пустой список
A = []

# Вводим список A из 10 ненулевых целых чисел
while len(A) < 10:
    try:
        number = int(input(f"Введите элемент A[{len(A)}]: "))
        if number == 0:
            raise ValueError("Число не должно быть нулевым. Попробуйте снова.")
        A.append(number)
    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, введите целое число.")

# Последний элемент списка
last_element = A[-1]

# Ищем первый элемент, который меньше последнего
result = 0  # По умолчанию, если не найдем, будет 0
for element in A:
    if element < last_element:
        result = element
        break  # Выходим из цикла, как только нашли первый подходящий элемент

# Выводим результат
print(result)
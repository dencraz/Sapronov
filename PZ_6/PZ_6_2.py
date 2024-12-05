def list_1(arr):
    try:
        if len(arr) < 2:
            raise ValueError("Список должен содержать как минимум два элемента.")

        min_diff = float('inf')  # Начальное значение для минимальной разности
        indices = (0, 1)  # Начальные индексы

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                diff = abs(arr[i] - arr[j])  # Вычисляем модуль разности
                if diff < min_diff:  # Если разность меньше минимальной
                    min_diff = diff
                    indices = (i, j)  # Обновляем индексы

        return sorted(indices)  # Возвращаем индексы в порядке возрастания

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

def main():
    try:
        input_list = input("Введите элементы списка, разделенные пробелами: ")
        arr = list(map(float, input_list.split()))  # Преобразуем ввод в список чисел

        b = list_1(arr)
        if b:
            print(f"Индексы двух ближайших элементов: {b}")

    except ValueError:
        print("Ошибка: Пожалуйста, введите только числа, разделенные пробелами.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()

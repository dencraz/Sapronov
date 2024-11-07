#Дано целое положительное число. Проверить истинность высказывания:
# «Данное число является четным двузначным»
try:
    a = int(input("Введите целое положительное число: "))
    if a <= 0:
        print("Ошибка: Введите положительное число.")
    else:
        # Проверка на двузначность и четность
        if 10 <= a <= 99 and not a % 2:
            print("Данное число является четным двузначным.")
        else:
            print("Данное число не является четным двузначным.")
except ValueError:
    print("Ошибка: Введите целое число.")

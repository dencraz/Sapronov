    #Даны три переменные вещественного типа: A, B, C.
    # Если их значения упорядочены по возрастанию, то удвоить их; в противном случае заменить
    # значение каждой переменной на противоположное.
    # Вывести новые значения переменных A, B, C.
while True:
    try:
        A = float(input("Введите значение A: "))
        B = float(input("Введите значение B: "))
        C = float(input("Введите значение C: "))
        break
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное вещественное число.")
if A <= B <= C:
    A *= 2
    B *= 2
    C *= 2
else:
    A = -A
    B = -B
    C = -C
print(f"Новые значения: A = {A}, B = {B}, C = {C}")









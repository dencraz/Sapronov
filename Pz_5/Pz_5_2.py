def PowerA3(e):
    c = e ** 3
    return c

def check(prompt):
    while True:
        try:
            a = float(input(prompt))
            return a
        except ValueError:
            print("Ошибка: Пожалуйста, введите числовое значение.")

n1 = check("Введите первое число: ")
n2 = check("Введите второе число: ")
n3 = check("Введите третье число: ")
n4 = check("Введите четвертое число: ")
n5 = check("Введите пятое число: ")

result1 = PowerA3(n1)
result2 = PowerA3(n2)
result3 = PowerA3(n3)
result4 = PowerA3(n4)
result5 = PowerA3(n5)

print(f"Третья степень {n1}: {result1}")
print(f"Третья степень {n2}: {result2}")
print(f"Третья степень {n3}: {result3}")
print(f"Третья степень {n4}: {result4}")
print(f"Третья степень {n5}: {result5}")
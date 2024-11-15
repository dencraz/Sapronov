# Дано целое число N (>0). Используя один цикл, найти сумму 1 + 1/(1!) + 1/(2!) +
# 1/(3!) + ... + 1/(N!) (выражение N! — N-факториал — обозначает произведение всех
# целых чисел от 1 до N: N! = 1-2-.. . N). Полученное число является приближенным
# значением константы e = exp(1).
def factorial(n):
    if n == 0 or n == 1:  # Базовый случай
        return 1
    return n * factorial(n - 1)

def  example_factorial(n): #функция
    sum_factorials = 0.0
    factorial = 1
    i = 0
    while i <= n:
        if i > 0:
            factorial *= i
        sum_factorials += 1 / factorial
        i += 1
    return sum_factorials

while True:
    try:
        n = int(input("Введите n факториал"))
        if n<0:
            print('Факторил не может быть отрицательным')
        else:
            print("-" * 35)
            print(f"Факториал {n} равен {factorial(n)}")
            print("-" * 35)
            print(f"1 + 1/(1!) + 1/(2!) + ... + 1/({n}!)")
            print(f"Ответ примера= {example_factorial(n)}")
            break
    except ValueError:
        print("Ошибка: Введено некорректное значение. Пожалуйста, введите правильное число.")

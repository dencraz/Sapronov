import random

matrix = (lambda x, y: [[random.randint(1, 10) for _ in range(x)] for _ in range(y)])


def summ(x,y):

    lst = matrix(x, y)
    print(f"Начальный список: {lst}".rjust(70)) 
    
    
    second_column = [row[1] for row in lst]

    squared = list(map(lambda x: x**2, second_column))

    for i, j in zip(second_column, squared):
        print(f"До: {i} После возведения: {j}".rjust(54))

while True:
    try:
        min_num = int(input('Введите минимальное значение >=2: '))
        
        if min_num >= 2:
            max_num=int(input('Введите максимальное значение '))
            print("-"*100)
            summ(min_num,max_num)
            break
        else:
            print("Число должно быть >= 2. Попробуйте еще раз.")
    except:
        print('Не правильный ввод')
    
    






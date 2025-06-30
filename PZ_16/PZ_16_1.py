# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows  
        self.cols = cols  
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]  

    def fill_matrix(self):

        print(f"Введите элементы матрицы {self.rows}x{self.cols}:")
        for i in range(self.rows):
            row = input(f"Строка {i + 1} (введите {self.cols} чисел через пробел): ").split()
            if len(row) != self.cols:
                print("Ошибка! Неверное количество элементов.")
                return False
            try:
                self.data[i] = [float(x) for x in row]  # поддерживаем дробные числа
            except ValueError:
                print("Ошибка! Вводите только числа.")
                return False
        return True

    def add(self, other):
        
        if self.rows != other.rows or self.cols != other.cols:
            print("Ошибка: матрицы должны быть одного размера!")
            return None
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def subtract(self, other):
        
        if self.rows != other.rows or self.cols != other.cols:
            print("Ошибка: матрицы должны быть одного размера!")
            return None
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def multiply(self, other):
        
        if self.cols != other.rows:
            print("Ошибка: число столбцов первой матрицы должно равняться числу строк второй!")
            return None
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum_val = 0
                for k in range(self.cols):
                    sum_val += self.data[i][k] * other.data[k][j]
                result.data[i][j] = sum_val
        return result

    def print_matrix(self):
       
        for row in self.data:
            print(" ".join([f"{x:5.1f}" for x in row]))  # форматированный вывод

def main():
    print("=== Калькулятор матриц ===")
    
    # Ввод размеров первой матрицы
    rows1 = int(input("Введите количество строк первой матрицы: "))
    cols1 = int(input("Введите количество столбцов первой матрицы: "))
    matrix1 = Matrix(rows1, cols1)
    if not matrix1.fill_matrix():
        return  # если ошибка ввода
        
    # Ввод размеров второй матрицы
    rows2 = int(input("\nВведите количество строк второй матрицы: "))
    cols2 = int(input("Введите количество столбцов второй матрицы: "))
    matrix2 = Matrix(rows2, cols2)
    if not matrix2.fill_matrix():
        return  # если ошибка ввода
    
    # Выбор операции
    print("\nВыберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    choice = input("Введите номер операции (1/2/3): ")
    
    result = None
    if choice == "1":
        result = matrix1.add(matrix2)
    elif choice == "2":
        result = matrix1.subtract(matrix2)
    elif choice == "3":
        result = matrix1.multiply(matrix2)
    else:
        print("Неверный выбор операции!")
        return
    
    if result:
        print("\nРезультат:")
        result.print_matrix()

if __name__ == "__main__":
    main()
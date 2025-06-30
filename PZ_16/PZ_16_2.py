#  Создание базового класса "Фигура" и его наследование для создания классов
# "Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
# такие как вычисление площади и периметра, а классы-наследники будут иметь
# специфичные методы и свойства.


import math

class Figure:
    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределен в подклассе")
    
    def perimeter(self):
        raise NotImplementedError("Метод perimeter() должен быть переопределен в подклассе")


class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть положительной")
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
    def diagonal(self):
        return self.side * math.sqrt(2)


class Rectangle(Figure):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Стороны прямоугольника должны быть положительными")
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def is_square(self):
        return self.length == self.width


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def diameter(self):
        return 2 * self.radius


def main():
    print("Выберите фигуру:")
    print("1 - Квадрат")
    print("2 - Прямоугольник")
    print("3 - Круг")
    
    choice = input("Введите номер фигуры (1/2/3): ")
    
    try:
        if choice == "1":
            side = float(input("Введите длину стороны квадрата: "))
            square = Square(side)
            print(f"\nКвадрат со стороной {side}:")
            print(f"Площадь: {square.area()}")
            print(f"Периметр: {square.perimeter()}")
            print(f"Диагональ: {square.diagonal():.2f}")
        
        elif choice == "2":
            length = float(input("Введите длину прямоугольника: "))
            width = float(input("Введите ширину прямоугольника: "))
            rectangle = Rectangle(length, width)
            print(f"\nПрямоугольник {length}x{width}:")
            print(f"Площадь: {rectangle.area()}")
            print(f"Периметр: {rectangle.perimeter()}")
            print(f"Это квадрат? {'Да' if rectangle.is_square() else 'Нет'}")
        
        elif choice == "3":
            radius = float(input("Введите радиус круга: "))
            circle = Circle(radius)
            print(f"\nКруг с радиусом {radius}:")
            print(f"Площадь: {circle.area():.2f}")
            print(f"Длина окружности: {circle.perimeter():.2f}")
            print(f"Диаметр: {circle.diameter()}")
        
        else:
            print("Ошибка: выбран неверный номер фигуры")
    
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
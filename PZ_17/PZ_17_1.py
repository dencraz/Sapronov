# Дано трехзначное число. Вывести число, полученное при прочтении
# исходного числа справа налево.

import tkinter as tk
from tkinter import messagebox

def check_number():
    try:
        a = int(entry.get())
        if a < 100 or a > 999:
            messagebox.showwarning("Ошибка", "Введено не трёхзначное число")
        else:
            messagebox.showinfo("Успех", "Введено трёхзначное число")
            # Вычисляем обратное число
            reversed_num = a % 10 * 100 + a % 100 // 10 * 10 + a // 100
            result_label.config(text=f"Обратное число: {reversed_num}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое число")

# Создаем главное окно
root = tk.Tk()
root.title("Проверка трёхзначного числа")
root.geometry("300x150")

# Создаем элементы интерфейса
label = tk.Label(root, text="Введите трёхзначное число:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

check_button = tk.Button(root, text="Проверить", command=check_number)
check_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Запускаем главный цикл
root.mainloop()
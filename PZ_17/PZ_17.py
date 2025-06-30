from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Test Form")
root.geometry("400x300")

# Создаем фрейм для основной части формы
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=BOTH, expand=True)

# Заголовок формы
title_label = ttk.Label(main_frame, text="Test Form", font=('Arial', 14, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Поля формы
fields = [
    ("Name", "entry"),
    ("Email", "entry"),
    ("Phone", "entry"),
    ("Gender", "combobox"),
    ("Age", "spinbox"),
    ("Comments", "text")
]   

for i, (label_text, field_type) in enumerate(fields, start=1):
    # Метка
    label = ttk.Label(main_frame, text=label_text + ":")
    label.grid(row=i, column=0, sticky=W, pady=2)
    
    # Поле ввода
    if field_type == "entry":
        entry = ttk.Entry(main_frame, width=30)
        entry.grid(row=i, column=1, sticky=EW, pady=2)
    elif field_type == "combobox":
        combo = ttk.Combobox(main_frame, values=["Male", "Female", "Other"], width=27)
        combo.grid(row=i, column=1, sticky=W, pady=2)
    elif field_type == "spinbox":
        spin = Spinbox(main_frame, from_=0, to=99, width=28)
        spin.grid(row=i, column=1, sticky=W, pady=2)
    elif field_type == "text":
        text = Text(main_frame, height=4, width=25)
        text.grid(row=i, column=1, sticky=W, pady=2)

# Фрейм для кнопок
button_frame = ttk.Frame(root, padding="10")
button_frame.pack(fill=X)


# Кнопки
submit_button = ttk.Button(button_frame, text="Submit")
submit_button.pack(side=LEFT, padx=5)

cancel_button = ttk.Button(button_frame, text="Cancel")
cancel_button.pack(side=LEFT, padx=5)

# Настройка растягивания колонок
main_frame.columnconfigure(1, weight=1)

root.mainloop()
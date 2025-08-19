import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Выпадающий список")

# Варианты для выпадающего списка
options = ["Опция 1", "Опция 2", "Опция 3"]

# Создание переменной для хранения выбранного значения
selected_option = tk.StringVar()

# Создание Combobox
combobox = ttk.Combobox(root, textvariable=selected_option, values=options)
combobox.pack(pady=20)

# Установка значения по умолчанию
combobox.set("Выберите опцию")

# Функция для обработки выбора
def show_selected_value():
    selected_value = selected_option.get()
    print(f"Выбрано: {selected_value}")
    # Можно добавить логику обработки выбранного значения

# Привязка функции к событию "выбор элемента в Combobox"
combobox.bind("<<ComboboxSelected>>", lambda event: show_selected_value())

root.mainloop()
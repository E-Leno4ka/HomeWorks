import os
import shutil
from time import sleep
import tkinter as tk
from tkinter import filedialog

def organize_files(directory):
    # Проверка, есть ли файлы в указанной папке
    if len(os.listdir(directory)):
        # Перебор всех файлов в выбранной директории
        for file in os.listdir(directory):
            # Проверка, является ли файл документом
            if file.lower().endswith((".doc", ".docx", ".odt")):
                # Создание полного пути к файлу
                filepath = os.path.join(directory, file)
                # Создание нового пути к директории для организации документов
                directory_new = os.path.join(directory, f"{directory}_new")
                # Создание новой директории, если она не существует
                if not os.path.exists(directory_new):
                    os.makedirs(directory_new)
                # Перемещение файла в новую директорию
                shutil.move(filepath, os.path.join(directory_new, file))
                # Вывод сообщения о перемещении файла
                tk.messagebox.showinfo("", f"Документ {file} успешно перемещён!")
            else:
                # Вывод сообщения о другом формате файла
                tk.messagebox.showinfo("", f"Файл {file} документом не является!")
        # Вывод сообщения о завершении организации документов
        tk.messagebox.showinfo("Готово", "Сортировка документов завершена!")
    else:
        tk.messagebox.showinfo("", f"Директория {directory} пуста!")
    sleep(2)
    window.destroy()

def choose_directory():
    # Открытие диалогового окна для выбора директории
    directory = filedialog.askdirectory()
    # Запуск функции перемещения документов, если была выбрана директория
    if directory:
        organize_files(directory)

# Создание основного окна Tkinter, его скрытие
window = tk.Tk()
window.withdraw()

# Запуск функции выбора директории
choose_directory()

window.mainloop()
import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Пример с прокруткой")

# Создание текстового виджета
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=10)

# Добавление текста (для демонстрации прокрутки)
text_area.insert(tk.INSERT, "Вот пример текста, который можно прокручивать.  \n" * 20)

root.mainloop()
from tkinter import *
from tkinter import ttk
import calculator_logic as c

def validate_entry():
    entry_text = entry.get()
    corrected_text = ''.join(b for b in entry_text if b in "0123456789.-")
    if entry_text != corrected_text:
        entry.delete(0, END)
        entry.insert(0, corrected_text)

def enter_number(number):
    entry.insert(END, number)

def set_operation(operation):
    global first
    global oper
    try:
        first = float(entry.get())
    except ValueError:
        first = 0
    oper = operation
    entry.delete(0, END)

def calc():
    second = float(entry.get())
    if oper == '+':
        result = c.add(first, second)
    elif oper == '-':
        result = c.subtract(first, second)
    elif oper == '*':
        result = c.multiply(first, second)
    elif oper == '/':
        result = c.divide(first, second)
    entry.delete(0, END)
    entry.insert(0, str(result))

def clear_entry():
    entry.delete(0, END)

# Создаем окно приложения
window = Tk()
window.title("Калькулятор")

entry = ttk.Entry(width=20)
entry.grid(row=0, column=0, columnspan=4, sticky="ew")
entry.bind('<KeyRelease>', lambda event: validate_entry())

# Цифровые кнопки
ttk.Button(text="1", command=lambda: enter_number('1')).grid(row=1, column=0)
ttk.Button(text="2", command=lambda: enter_number('2')).grid(row=1, column=1)
ttk.Button(text="3", command=lambda: enter_number('3')).grid(row=1, column=2)
ttk.Button(text="4", command=lambda: enter_number('4')).grid(row=2, column=0)
ttk.Button(text="5", command=lambda: enter_number('5')).grid(row=2, column=1)
ttk.Button(text="6", command=lambda: enter_number('6')).grid(row=2, column=2)
ttk.Button(text="7", command=lambda: enter_number('7')).grid(row=3, column=0)
ttk.Button(text="8", command=lambda: enter_number('8')).grid(row=3, column=1)
ttk.Button(text="9", command=lambda: enter_number('9')).grid(row=3, column=2)
ttk.Button(text="0", command=lambda: enter_number('0')).grid(row=4, column=1)

# Кнопки арифметических операций
ttk.Button(text="+", command=lambda: set_operation('+')).grid(row=1, column=3)
ttk.Button(text="-", command=lambda: set_operation('-')).grid(row=2, column=3)
ttk.Button(text="*", command=lambda: set_operation('*')).grid(row=3, column=3)
ttk.Button(text="/", command=lambda: set_operation('/')).grid(row=4, column=3)
ttk.Button(text="^2", command=lambda: set_operation('^2')).grid(row=5, column=3)

# Кнопка равно и очистки
ttk.Button(text="=", command=calc).grid(row=5, column=2)
ttk.Button(text="C", command=clear_entry).grid(row=5, column=1)

# Кнопка точки
ttk.Button(text=".", command=lambda: enter_number('.')).grid(row=5, column=0)

first = 0
oper = 0

window.mainloop()

from tkinter import *
from tkinter import messagebox as mb

def summ():
    n1 = e1.get()
    if not n1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено целое число")
        return  # Возвращаемся из функции, если ввод некорректен
    n2 = e2.get()
    if not n2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено целое число")
        return  # Возвращаемся из функции, если ввод некорректен
    n3 = e3.get()
    if not n3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В третье поле должно быть введено целое число")
        return  # Возвращаемся из функции, если ввод некорректен

    t1 = int(n1)
    t2 = int(n2)
    t3 = int(n3)
    sum = t1 + t2 + t3
    m1['text'] = f"{n1} + {n2} + {n3} = {str(sum)}"
        
    answer = mb.askretrycancel(title="Вопрос", message="Продолжить вычисления?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()

def pr():
    n1 = e1.get()
    if not n1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено целое число")
        return  # Возвращаемся из функции, если ввод некорректен
    n2 = e2.get()
    if not n2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено целое число")
        return  # Возвращаемся из функции, если ввод некорректен
    n3 = e3.get()
    if not n3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В третье поле должно быть введено целое число")
        return  # Возвращаемся из функции, если ввод некорректен

    mult1 = int(n1)
    mult2 = int(n2)
    mult3 = int(n3)
    pr = mult1 * mult2 * mult3
    m1['text'] = f"{n1} * {n2} * {n3} = {str(pr)}"
        
    answer = mb.askretrycancel(title="Вопрос", message="Продолжить вычисления?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()

window = Tk()
window.title("Калькулятор")
m = Label(height=3, text="Введите три числа и нажмите на кнопку для вычисления суммы или произведения.")
m.pack()
e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()
e3 = Entry()  # Добавление третьего поля для ввода
e3.pack()
b1 = Button(text="Сложить три числа", command=summ)
b1.pack()
b2 = Button(text="Умножить три числа", command=pr)
b2.pack()
m1 = Label(height=3)
m1.pack()
window.mainloop()
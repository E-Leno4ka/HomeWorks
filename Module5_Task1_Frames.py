#import tkinter as tk
from tkinter import *

def read_name():
    Name = e.get().capitalize()  # получаем введенный текст
    print(Name)     # выводим  введенный текст

def read_surname():
    Surname = e2.get().capitalize()  # получаем введенный текст
    print(Surname)     # выводим  введенный текст

def read_patronymic():
    Patronymic = e3.get().capitalize()  # получаем введенный текст
    print(Patronymic)     # выводим  введенный текст
    
window = Tk(className="Представьтесь, пожалуйста")
f1 = Frame()
f2 = Frame()
f3 = Frame()
f1.pack()
f2.pack()
f3.pack()

m = Label(f1, text="Введите имя  : ", bg="grey", font='Courier 16 bold')
m.pack(side=LEFT)
e = Entry(f1, width=21, justify="left", bg="grey",
          fg="brown", font='Courier 18 bold')
e.pack(side=LEFT)
b = Button(f1, text="Ввод", bg="grey", font=('Courier 12 bold'), command=read_name)
b.pack()

m2 = Label(f2, text="Введите фамилию: ", bg="grey", font='Courier 16 bold')
m2.pack(side=LEFT)
e2 = Entry(f2, width=19, justify="left", bg="grey",
          fg="brown", font='Courier 18 bold')
e2.pack(side=LEFT)
b2 = Button(f2, text="Ввод", bg="grey", font=('Courier 12 bold'), command=read_surname)
b2.pack()

m3 = Label(f3, text="Введите отчество: ", bg="grey", font='Courier 16 bold')
m3.pack(side=LEFT)
e3 = Entry(f3, width=18, justify="left", bg="grey",
          fg="brown", font='Courier 18 bold')
e3.pack(side=LEFT)
b3 = Button(f3, text="Ввод", bg="grey", font=('Courier 12 bold'), command=read_patronymic)
b3.pack()

window.mainloop()

from tkinter import *
from tkinter import messagebox as mb

def book_seat(event=None):
    """
    Эта функция бронирует место
    """
    s = seat_entry.get().upper()
    try:
        if seats[s] == "свободно":
            seats[s] = "забронировано"
            update_canvas()
            mb.showinfo("Успех", f"Место {s} успешно забронировано.")
        else:
            mb.showerror("Ошибка", f"Место {s} уже забронировано.")
    except KeyError:
        mb.showerror("Ошибка", f"Место {s} не существует.")

def cancel_booking(event=None):
    """
    Эта функция отменяет бронирование места (освобождает забронированное)
    """
    s = cancel_seat_entry.get().upper()
    try:
        if seats[s] == "забронировано":
            seats[s] = "свободно"
            update_canvas()
            mb.showinfo("Успех", f"Бронь на месте {s} успешно отменена.")
        else:
            mb.showerror("Ошибка", f"Место {s} не забронировано или не существует.")
    except KeyError:
        mb.showerror("Ошибка", f"Место {s} не существует.")

def update_canvas():
    """
    Эта функция обновляет виджет со схемой мест
    """
    canvas.delete("all")
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = "green" if status == "свободно" else "red"
        canvas.create_rectangle(x, y, x+30, y+30, fill=color)
        canvas.create_text(x+15, y+15, text=seat)
        
# Создание основного окна
window = Tk()
window.title("Бронирование мест")
window.geometry("400x320")

# Создание виджета со схемой мест
canvas = Canvas(width=400, height=50)
canvas.pack(pady=10)

seats = {f"Б{i}": "свободно" for i in range(1, 10)}
update_canvas()

# Добавление легенды
canvas1 = Canvas(width=400, height=50)
canvas1.pack(pady=10)
canvas1.create_rectangle(10, 2, 40, 32, fill="green")
canvas1.create_text(80, 17, text="Свободно")
canvas1.create_rectangle(160, 2, 190, 32, fill="red")
canvas1.create_text(245, 17, text="Забронировано")

# Добавление поля ввода и кнопки для бронирования
seat_entry = Entry()
seat_entry.pack(pady=5)
seat_entry.focus()
seat_entry.bind("<Return>", book_seat)
Button(text="Забронировать место", command=book_seat).pack(pady=5)

# Добавление поля ввода и кнопки для отмены бронирования
cancel_seat_entry = Entry()
cancel_seat_entry.pack(pady=10)
cancel_seat_entry.bind("<Return>", cancel_booking)
Button(text="Отменить бронь", command=cancel_booking).pack(pady=10)

window.mainloop()
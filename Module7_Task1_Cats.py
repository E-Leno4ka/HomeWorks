from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Список доступных тегов
ALLOWED_TAGS = [
    '', 'sleep', 'jump', 'smile', 'fight', 'black', 'white', 'red', 'siamese', 'bengal', 'cute'
]

def load_image(url):
    '''
    Загружает данные с сайта url и преобразует их в изображение
    '''
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None

def open_new_window():
    '''
    Открывает в новом окне загруженное изображение с сайта url (с тегом или без)
    '''
    tag = tag_combobox.get()
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_with_tag)
    if img:
        new_window = Toplevel()
        new_window.title(f"{tag.capitalize()} Cat Image")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.image = img
        label.pack()

def random_cat():
    '''
    Открывает в новом окне случайное изображение с сайта url
    '''
    img = load_image('https://cataas.com/cat')
    if img:
        new_window = Toplevel()
        new_window.title("Random Cat Image")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.image = img
        label.pack()

# Создание основного окна программы
window = Tk()
window.title("Cats!")
window.geometry("400x150")

# Добавление кнопки "Меню"
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Наполнение выпадающего меню
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.destroy)

# Рамки для организации виджетов в окне программы
f1 = Frame(padx=35)
f2 = Frame(padx=35)
f1.pack(side=LEFT)
f2.pack(side=RIGHT)

# Метка "Выбери тег"
tag_label = Label(f1, text="Выбери тег")
tag_label.pack()

# Окошко выбора тега
tag_combobox = ttk.Combobox(f1, values=ALLOWED_TAGS)
tag_combobox.pack()

# Кнопка загрузки случайного изображения котика
rand_c = Button(f2, text="Случайный котик", command=lambda: random_cat())
rand_c.pack()

window.mainloop()
 
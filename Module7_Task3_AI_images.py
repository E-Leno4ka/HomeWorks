import asyncio
from g4f.client import AsyncClient
import requests
import tkinter as tk
from tkinter import Tk, Toplevel, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
from translate import Translator

tabs = []
txt_prompt = ""

def get_prompt():
    '''
    Эта функция получает текст из поля ввода и
    переводит его с русского на английский язык
    '''
    global txt_prompt
    translator = Translator(from_lang="ru", to_lang="en")
    txt_prompt = translator.translate(user_input.get())

async def main():
    '''
    Отправляет ИИ текстовый запрос, получает ссылку на изображение.
    '''
    client = AsyncClient()

    get_prompt()
    response = await client.images.generate(
        prompt=txt_prompt,
        model="flux",
        response_format="url"
        # Add any other necessary parameters
    )

    image_url = response.data[0].url
    return image_url

def show_image():
    '''
    Эта фнукция запрашивает данные по ссылке,
    преобразует их в изображение
    и выводит на новой вкладке в отдельном окне
    '''
    image_url = asyncio.run(main())

    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img_size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(img_size)
            img = ImageTk.PhotoImage(img)

            tab = ttk.Frame(notebook)
            notebook.add(tab, text=f"Изображение {notebook.index('end') + 1}")
            tabs = notebook.tabs()
            label = ttk.Label(tab, image=img)
            label.image = img
            label.pack(padx=10, pady=10)

            last_tab_index = len(tabs) - 1
            notebook.select(last_tab_index) # делает активной вкладку с последним загруженным изображением
        except requests.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

def clear_tabs():
    '''
    Эта функция "забывает" открытые вкладки окна "Изображения".
    '''
    global tabs
    global button2
    tabs = notebook.tabs()
    for tab in tabs:
        notebook.forget(tab)

window = Tk()
window.title("Генератор изображений")

label_text = ttk.Label(window, text="Введите запрос")
label_text.pack()

user_input = tk.StringVar()
entry_widget = ttk.Entry(window, textvariable=user_input)
entry_widget.pack()

frame1 = ttk.Frame(window, )
frame1.pack(padx=10, pady=5)
button = ttk.Button(frame1, text="Отправить", command=show_image)
button.pack(padx=10, pady=5)

button2 = ttk.Button(frame1, text="Очистить вкладки", command=clear_tabs)
button2.pack(padx=10, pady=5)

width_label = ttk.Label(window, text="Ширина:")
width_label.pack(side='left', padx=(10, 0))
width_spinbox = ttk.Spinbox(window, from_=200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0, 10))

height_label = ttk.Label(window, text="Высота:")
height_label.pack(side='left', padx=(10, 0))
height_spinbox = ttk.Spinbox(window, from_=200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0, 10))

# Создаем отдельное окно для Notebook
top_level_window = Toplevel(window)
top_level_window.title("Изображения")

notebook = ttk.Notebook(top_level_window)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

window.mainloop()
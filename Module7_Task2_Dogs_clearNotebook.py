import requests
from tkinter import Tk, Toplevel, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

tabs = []

def get_random_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        return data['message']
    except requests.RequestException as e:
        messagebox.showerror("Ошибка", f"Ошибка при запросе к API: {e}")
        return None

def show_image():
    global tabs
    status_label.config(text="Загрузка...")
    image_url = get_random_dog_image()

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
            new_button() # добавляем кнопку в основном окне
            tabs = notebook.tabs()
            label = ttk.Label(tab, image=img)
            label.image = img
            label.pack(padx=10, pady=10)

            status_label.config(text="")
            last_tab_index = len(tabs) - 1
            notebook.select(last_tab_index) # делает активной вкладку с последним загруженным изображением
        except requests.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")

def start_progress():
    progress['value'] = 0
    progress.start(30)
    window.after(3000, lambda: [progress.stop(), show_image()])

def new_button():
    '''
    Эта функция добавляет в основном окне кнопку "Очистить вкладки"
    после создания хотя бы одной вкладки в окне "Изображения пёсиков".
    '''
    global tabs
    global button2
    last_tab_index = len(tabs) - 1
    if last_tab_index == -1:
        button2 = ttk.Button(frame1, text="Очистить вкладки", command=clear_tabs)
        button2.pack(padx=10, pady=5)

def clear_tabs():
    '''
    Эта функция "забывает" открытые вкладки окна "Изображения пёсиков"
    и удаляет кнопку "Очистить вкладки" с основного окна.
    '''
    global tabs
    global button2
    tabs = notebook.tabs()
    for tab in tabs:
        notebook.forget(tab)
    button2.destroy()
    tabs = []

window = Tk()
window.title("Случайное изображение")

status_label = ttk.Label(window, text="")
status_label.pack(padx=10, pady=5)

frame1 = ttk.Frame(window, )
frame1.pack(padx=10, pady=5)
button = ttk.Button(frame1, text="Загрузить изображение", command=start_progress)
button.pack(padx=10, pady=5)

progress = ttk.Progressbar(window, mode='determinate', length=300)
progress.pack(padx=10, pady=5)

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
top_level_window.title("Изображения пёсиков")

notebook = ttk.Notebook(top_level_window)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

window.mainloop()
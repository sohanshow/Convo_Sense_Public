import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style

import canvas
from ttkthemes import ThemedTk
from tkinter import Toplevel, Label, PhotoImage
from PIL import Image, ImageTk

from tkinter import Canvas, Scrollbar


from threading import Thread

from bs4 import BeautifulSoup

# Your existing app.py content
# ...

word_data = {
}

def add_word(word, definition, image):
    word_data[word] = {
        "definition": definition,
        "image": image,
    }
    create_button(word, word_data[word])

def show_word_data(word, data):
    top = Toplevel()
    top.title(word)

    word_label = Label(top, text=f"{word.capitalize()}:", font=("Arial", 20))
    word_label.pack(pady=10)

    # Remove HTML tags from the definition
    soup = BeautifulSoup(data['definition'], 'html.parser')
    definition_text = soup.get_text()

    definition_label = Label(top, text=f"Definition: {definition_text}")
    definition_label.pack(pady=10)

    # Open image file and get its dimensions
    image = Image.open(data["image"])
    width, height = image.size

    # Resize image to fit the width of the label while maintaining aspect ratio
    label_width = 400
    resize_factor = label_width / width
    new_width = int(width * resize_factor)
    new_height = int(height * resize_factor)
    image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # Create a PhotoImage object from the resized image
    photo = ImageTk.PhotoImage(image)

    image_label = Label(top, image=photo)
    image_label.image = photo  # Keep a reference to prevent garbage collection
    image_label.pack(pady=10)


def create_button(word, data):
    button = ttk.Button(
        frame,
        text=word.capitalize(),
        command=lambda w=word, d=data: show_word_data(w, d),
        width=20,
    )
    button.pack(pady=5)
#
# def on_mouse_wheel(event):
#     main_canvas.yview_scroll(-1 * int(event.delta / 120), "units")

def main():
    global frame
    root = ThemedTk(theme="arc")  # You can choose other themes like 'equilux', 'clearlooks', etc.
    root.title("Word Dictionary")
    root.geometry("800x600")  # Set the initial window size to 800x600

    style = Style()
    style.configure("TButton", font=("Arial", 12), padding=5)

    # Create a canvas and add a scrollbar
    main_canvas = Canvas(root)
    main_canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    scrollbar = Scrollbar(root, orient="vertical", command=main_canvas.yview)
    scrollbar.pack(side="left", fill="y")

    main_canvas.configure(yscrollcommand=scrollbar.set)
    main_canvas.bind("<Configure>", lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

    def on_mouse_wheel(event):
        main_canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    # Bind the mouse wheel event to the canvas
    main_canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    # Create a frame inside the canvas
    frame = ttk.Frame(main_canvas)
    main_canvas.create_window((0, 0), window=frame, anchor="nw")

    for word, data in word_data.items():
        create_button(word, data)

    # Example: Adding a new word to the dictionary and updating the GUI
    #add_word("orange", "A round, orange-colored citrus fruit with a tough, slightly bumpy rind.", "orange_image.png")

    root.mainloop()

listen_thread = Thread(target=main)
listen_thread.start()
"""create an app that helps you access your sites, or folders faster """
import tkinter as tk
import webbrowser
from PIL import ImageTk
import os
from pathlib import Path


def open_you_tube():
    """create a function that returns the link you want to access it"""
    webbrowser.open('www.youtube.com')


def open_folder():
    """create a function that open a specify folder"""
    folder_path = Path(__file__).parent
    os.startfile(folder_path)


def open_google():
    """create a function to open google
        and put it inside the button
    """
    webbrowser.open('www.google.com')


def open_netflix():
    """create a function to open netflix"""
    webbrowser.open('www.netflix.com')


def open_instagram():
    """create a function to oprn instagram"""
    webbrowser.open('www.instagram.com')


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    root.title("my app")
    root.iconbitmap('logo.ico')
    root.configure(bg='#0F5B92')

    my_image = ImageTk.PhotoImage(
        file=Path(__file__).parent / 'logo_play.png')
    image_label = tk.Label(root, image=my_image, width=150, height=150)
    image_label.image = my_image
    image_label.grid(row=4, column=5, padx=200, pady=20)

    button = tk.Button(root, text='YouTube', font=('Arial Bolt', 10),
                       width=30, command=open_you_tube)
    button.grid(row=0, column=1, padx=10, pady=10)

    button_2 = tk.Button(root, text='Folders', font=('Arial Bolt', 10),
                         width=30, command=open_folder)
    button_2.grid(row=2, column=1, padx=10, pady=10)

    button_3 = tk.Button(root, text='Google', font=('Arial Bolt', 10),
                         width=30, command=open_google)
    button_3.grid(row=4, column=1, padx=10, pady=10)

    button_4 = tk.Button(root, text='Netflix', font=('Arial Bolt', 10),
                         width=30, command=open_netflix)
    button_4.grid(row=6, column=1, padx=10, pady=10)

    button_5 = tk.Button(root, text='Instagram', font=('Arial Bolt', 10),
                         width=30, command=open_instagram)
    button_5.grid(row=8, column=1, padx=10, pady=10)

    presentation_label = tk.Label(root, text='choose your link',
                                  font=('Arial Bolt', 16), bg='#0F5B92')
    presentation_label.grid(row=10, column=1, padx=10, pady=10)

    image_label.grid_propagate(False)

    root.mainloop()

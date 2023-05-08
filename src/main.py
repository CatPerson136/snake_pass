####################################

# Snake Pass

# Copyright (C) 2023 Andrew Smith. GNU General Public License v3

# License: https://www.gnu.org/licenses/gpl-3.0.en.html

####################################

import customtkinter as ctk
import random
import string
from hashlib import sha512
import tkinter as tk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


def set_password_and_print_it_out():
    # Gets 8 random ascii charters and adds to a string.
    password = sha512(
        f"{random.choices(string.ascii_letters, k=8)}".encode("utf-8")
    ).hexdigest()

    password_to_string = tk.StringVar()
    password_to_string.set(password)

    # A text entry to print the password and allows it to be copied.
    password_text_entry = ctk.CTkEntry(
        master=app, width=160, height=40, textvariable=password_to_string
    ).place(relx=0.5, rely=0.3, anchor=ctk.CENTER)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Snake Pass")
        self.geometry("350x300")  # this is the size of the window

        # A button to generate a radom password when clicked.
        self.btn = ctk.CTkButton(
            self, text="Generate", command=set_password_and_print_it_out
        ).place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


app = App()
app.mainloop()

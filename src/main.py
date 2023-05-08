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


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Snake Pass")
        self.geometry("350x300")  # this is the size of the window

        # A button to generate a radom password when clicked.
        self.btn = ctk.CTkButton(
            self, text="Generate", command=self.set_password_and_print_it_out
        ).place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def set_password_and_print_it_out(self):
        # Gets 8 random ascii charters and adds to a string.
        self.password = sha512(
            f"{random.choices(string.ascii_letters, k=8)}".encode("utf-8")
        ).hexdigest()

        self.password_to_string = tk.StringVar()
        self.password_to_string.set(self.password)

        # A text entry to print the password and allows it to be copied.
        self.password_text_entry = ctk.CTkEntry(
            master=app, width=160, height=40, textvariable=self.password_to_string
        ).place(relx=0.5, rely=0.3, anchor=ctk.CENTER)


app = App()
app.mainloop()

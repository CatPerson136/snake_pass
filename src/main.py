####################################

# Snake Pass

# Copyright (C) 2023 Andrew Smith. GNU General Public License v3

# License: https://www.gnu.org/licenses/gpl-3.0.en.html

####################################

from typing import Optional, Tuple, Union
import customtkinter as ctk
from password import Password

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Snake Pass")
        self.geometry("350x300")

        self.btn = ctk.CTkButton(
            self, text="Generate", command=Password.generate_string
        ).place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


app = App()
app.mainloop()

####################################

# Snake Pass

# Copyright (C) 2023 Andrew Smith. GNU General Public License v3

# License: https://www.gnu.org/licenses/gpl-3.0.en.html

####################################

import customtkinter as ctk
import random
import string

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Snake Pass")
        self.geometry("350x300")  # this is the size of the window

        self.btn = ctk.CTkButton(
            self, text="Generate", command=App.set_password_and_print_it_out
        ).place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def set_password_and_print_it_out():
        # gets 8 random ascii charters.
        random_string = "".join(random.choices(string.ascii_letters, k=8))

        # gets 4 random numbers.
        random_int = "".join(random.choices(string.digits, k=4))

        # Adds it to a f string and prints it out.
        password = f"{random_string}{random_int}"
        print(password)


app = App()
app.mainloop()

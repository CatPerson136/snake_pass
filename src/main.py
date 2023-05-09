####################################

# Snake Pass

# Copyright (C) 2023 Andrew Smith. GNU General Public License v3

# License: https://www.gnu.org/licenses/gpl-3.0.en.html

####################################

import customtkinter as ctk
import random
import string
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
        ).place(relx=0.28, rely=0.5, anchor=ctk.CENTER)

        # A button to copy the password to your clipboard.
        self.copy_btn = ctk.CTkButton(
            self, text="Copy", command=self.copy_password_to_clipboard
        ).place(relx=0.72, rely=0.5, anchor=ctk.CENTER)

    def copy_password_to_clipboard(self):
        # Copies the generated password to the clipboard.
        self.clipboard_clear()
        self.clipboard_append(self.password)

    # Gets 32 random ascii characters (uppercase, lowercase, digits, and punctuation)
    def set_password_and_print_it_out(self):
        self.password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=32))

        self.password_to_string = tk.StringVar()
        self.password_to_string.set(self.password)

        # A text entry to print the password and allows it to be copied.
        self.password_text_entry = ctk.CTkEntry(
            master=app, width=260, height=40, textvariable=self.password_to_string
        ).place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

app = App()
app.mainloop()

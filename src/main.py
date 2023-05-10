####################################

# Snake Pass

# Copyright (C) 2023 Andrew Smith. GNU General Public License v3

# License: https://www.gnu.org/licenses/gpl-3.0.en.html

####################################

import customtkinter as ctk
<<<<<<< HEAD
import random
import string
import tkinter as tk
=======
import tkinter as tk
import subprocess as sb
>>>>>>> main

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

<<<<<<< HEAD
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Snake Pass")
        self.geometry("350x300")  # this is the size of the window

        # A label and input box for password length
        self.length_label = ctk.CTkLabel(self, text="Password length:").place(relx=0.3, rely=0.64, anchor=ctk.CENTER)
        self.length_input = ctk.CTkEntry(self, width=36)
        self.length_input.place(relx=0.5, rely=0.64, anchor=ctk.CENTER)

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

    def set_password_and_print_it_out(self):
        # Gets the length of the password from the input box.
        length_str = self.length_input.get()
        try:
            length = int(length_str)
        except ValueError:
            # If the input is not a valid integer, use the default length of 32.
            length = 32
            self.length_input.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        # Generates a random password with the specified length.
        self.password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=length))

        self.password_to_string = tk.StringVar()
        self.password_to_string.set(self.password)

        # A text entry to print the password and allows it to be copied.
        self.password_text_entry = ctk.CTkEntry(
            master=app, width=260, height=40, textvariable=self.password_to_string
        ).place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
=======
window = ctk.CTk()

window.geometry("350x300")  # this is window size
window.title("Snake Pass")

"""
* This button will start the java file.
* Which is RandomPassword.java
"""

# This will run the java file then print it on a label.
def generate_string():
    output = sb.check_output(["java", "com/cat/RandomPassword.java"])
    f = output.decode("utf-8")
    str_var = tk.StringVar()
    str_var.set(f)
    output_label = ctk.CTkEntry(
        master=window, textvariable=str_var, width=250, height=40
    ).place(relx=0.5, rely=0.3, anchor=ctk.N)

btn = ctk.CTkButton(master=window, text="Generate", command=generate_string).place(
    relx=0.5, rely=0.5, anchor=ctk.CENTER
)
>>>>>>> main

window.mainloop()

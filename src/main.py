####################################

# Snake Pass

# Copyright (C) 2023 Andrew Smith. GNU General Public License v3

# License: https://www.gnu.org/licenses/gpl-3.0.en.html

####################################

import customtkinter as ctk
import tkinter as tk
import subprocess as sb

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

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

window.mainloop()

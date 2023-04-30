####################################

# Snake Pass

# Copyright (C) 2023 Andrew Smith. GNU General Public License v3

# License: https://www.gnu.org/licenses/gpl-3.0.en.html

####################################

import customtkinter as ctk
import subprocess as sb


# This will run the java file then print it on a label.
def generate_string():
    output = sb.check_output(["java", "com/cat/RandomPassword.java"])
    output_label.configure(text="rrrrrr")


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()

window.geometry("300x300")  # this is window size
window.title("Snake Pass")
"""
* This button will start the java file.
* Which is RandomPassword.java
"""

# Generate button
btn = ctk.CTkButton(master=window, text="Start", command=generate_string).place(
    relx=0.5, rely=0.5, anchor=ctk.CENTER
)

# This will display the password in the label
output_label = ctk.CTkLabel(master=window, text="").place(
    relx=0.5, rely=0.3, anchor=ctk.N
)

window.mainloop()

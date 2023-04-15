####################################

# Snake Pass

# Copyright (C) 2023 Andrew Smith. GNU General Public License v3

# License: https://www.gnu.org/licenses/gpl-3.0.en.html

####################################

# Importing the GUI module for the app.
import customtkinter as ctk

# Setting the theme and the colour scheme.
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Top of the window code.
window = ctk.CTk()

window.geometry("300x300CatPerson136")  # this is window size
window.title("Key Reader")  # this is the window title

# This button will start the java file.
# Which is KeyReader.java
btn = ctk.CTkButton(master=window, text="Start").place(
    relx=0.5, rely=0.5, anchor=ctk.CENTER
)

# This the label to capture the key inputs and display them.
# label = ctk.CTkLabel()

window.mainloop()  # Buttom of the window code.

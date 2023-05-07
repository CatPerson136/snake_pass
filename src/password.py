import customtkinter as ctk
import random


class Password:
    # This will run the java file then print it on a label.
    def generate_string():
        r = random.randint(1, 100)
        output = ctk.CTkEntry(master=window, width=160, height=40, text=r).pack()

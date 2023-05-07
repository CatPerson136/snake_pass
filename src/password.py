import customtkinter as ctk
import random
import string


class RandomPassword:
    def __init__(self) -> None:
        self.password = random.choices(string.ascii_letters) + str(random.randint(0, 9))
        print(self.password)


RandomPassword()

import customtkinter as ctk

class Button:
    def __init__(self, parent, text, command=None, width=200, height=40, corner_radius=10):
        self.button = ctk.CTkButton(parent, text=text, command=command, width=width, height=height, corner_radius=corner_radius)
    
    def pack(self, *args, **kwargs):
        self.button.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self.button.grid(*args, **kwargs)

    def configure(self, **kwargs):
        self.button.configure(**kwargs)

class Label:
    def __init__(self, parent, text, font=("Arial", 14), text_color="white"):
        self.label = ctk.CTkLabel(parent, text=text, font=font, text_color=text_color)
    
    def pack(self, *args, **kwargs):
        self.label.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self.label.grid(*args, **kwargs)

    def configure(self, **kwargs):
        self.label.configure(**kwargs)

class Slider:
    def __init__(self, parent, from_=0, to=100, number_of_steps=10, width=250):
        self.slider = ctk.CTkSlider(parent, from_=from_, to=to, number_of_steps=number_of_steps, width=width)

    def pack(self, *args, **kwargs):
        self.slider.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self.slider.grid(*args, **kwargs)

    def configure(self, **kwargs):
        self.slider.configure(**kwargs)

class CheckBox:
    def __init__(self, parent, text, command=None):
        self.checkbox = ctk.CTkCheckBox(parent, text=text, command=command)

    def pack(self, *args, **kwargs):
        self.checkbox.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self.checkbox.grid(*args, **kwargs)

    def configure(self, **kwargs):
        self.checkbox.configure(**kwargs)

import customtkinter as ctk

class Window:
    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height

    def render(self):
        """Renderuje wszystkie elementy okna"""
        self.root.geometry(f"{self.width}x{self.height}")

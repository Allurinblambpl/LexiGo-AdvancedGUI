import keyboard
import mouse

class InputHandler:
    def __init__(self, root):
        self.root = root
        self.keys = {'w': False, 'a': False, 's': False, 'd': False}

        # Obsługuje kliknięcia myszką
        self.root.bind("<Button-1>", self.mouse_click)

    def handle_key_press(self, event):
        """Obsługuje naciśnięcia klawiszy"""
        if event.char == 'w':
            self.keys['w'] = True
        elif event.char == 'a':
            self.keys['a'] = True
        elif event.char == 's':
            self.keys['s'] = True
        elif event.char == 'd':
            self.keys['d'] = True

    def mouse_click(self, event):
        """Reaguje na kliknięcie myszy"""
        print(f"Mouse clicked at {event.x}, {event.y}")

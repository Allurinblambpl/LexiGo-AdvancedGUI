import customtkinter as ctk
from components import Button, Label, Slider, CheckBox
from events import ButtonEvents

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        """Tworzymy wszystkie widgety na GUI"""
        self.root.geometry("800x600")
        self.root.title("LexiGo - GUI Creator")

        # Nagłówek
        self.header_label = Label(self.root, text="Welcome to LexiGo GUI Creator!", font=("Arial", 20, "bold"))
        self.header_label.pack(pady=30)

        # Przycisk
        self.greet_button = Button(self.root, text="Greet", command=ButtonEvents.greet)
        self.greet_button.pack(pady=20)
        
        # Etykieta
        self.label = Label(self.root, text="Explore the new GUI features", font=("Arial", 16))
        self.label.pack(pady=20)

        # Suwak
        self.volume_slider = Slider(self.root, from_=0, to=100)
        self.volume_slider.pack(pady=10)

        # Checkbox
        self.feature_checkbox = CheckBox(self.root, text="Enable Feature", command=self.checkbox_action)
        self.feature_checkbox.pack(pady=10)

    def checkbox_action(self):
        """Reakcja na kliknięcie checkboxa"""
        if self.feature_checkbox.checkbox.get():
            print("Feature enabled")
        else:
            print("Feature disabled")

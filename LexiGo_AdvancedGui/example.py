import customtkinter as ctk
from gui import SimpleGUI

def main():
    
    root = ctk.CTk()
    root.title("Advanced GUI Application")

    
    root.geometry("800x600")

    
    gui = SimpleGUI(root)

    
    root.mainloop()

if __name__ == "__main__":
    main()

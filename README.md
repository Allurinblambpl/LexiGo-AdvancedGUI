# LexiGo GUI

**LexiGo GUI** is an advanced graphical user interface (GUI) framework built using the `customtkinter` library. This package allows you to easily create modern, interactive, and aesthetically pleasing user interfaces for Python applications. 

It provides a collection of customizable components such as buttons, labels, sliders, and checkboxes that users can combine to create their own GUI applications.

## Features
- **Modern look**: Customizable themes with support for light and dark modes.
- **Interactive components**: Buttons, checkboxes, labels, sliders.
- **Easy to use**: Simple API for creating GUI elements and handling events.
- **Fully customizable**: Change colors, fonts, and other properties of components.
- **Cross-platform**: Works on Windows, macOS, and Linux.

## Installation

You can install **LexiGo GUI** using `pip`:

pip install LexiGo-GUI



# Example: Creating a Simple GUI

from tkinter import Tk
from LexiGo_GUI import SimpleGUI

def main():
    root = Tk()
    gui = SimpleGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()



# Customizing Components
You can customize the components easily by configuring properties like background color, text color, font, and more.


from LexiGo_GUI.components import Button, Label, Slider

# Create a button with customized text and colors
button = Button(parent_window, text="Click Me!", width=200, height=50)
button.configure(fg_color="blue", text_color="white", font=("Arial", 14))

# Create a slider with custom range
slider = Slider(parent_window, from_=0, to=100, number_of_steps=10)
slider.pack()

# Create a label with custom text
label = Label(parent_window, text="Hello, welcome to LexiGo!", font=("Arial", 20, "bold"))
label.pack()


# Available Components
Button: Create buttons with text, background color, font, and hover effect.
Label: Create labels with customizable text and fonts.
Slider: A slider for numeric input with adjustable steps.
CheckBox: A checkbox that users can select or deselect.



# Requirements
Python 3.x
customtkinter library
To install dependencies, run:

pip install customtkinter
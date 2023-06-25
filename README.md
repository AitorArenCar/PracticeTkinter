# PracticeTkinter
Simple GUI to practice the use of Tkinter on Python.

# README

This is a simple Python project that demonstrates the usage of the `Interfaz` and `Operaciones` classes.

## Project Structure

The project consists of two files:

- `programa.py`: It contains the main program logic and the `Interfaz` class for the graphical user interface.
- `operaciones.py`: It defines the `Operaciones` class, which contains methods to perform mathematical operations on a given number.

## Usage

To use the project in your own Python program, follow these steps:

1. Copy the contents of `programa.py` and `operaciones.py` into your Python files.

2. Import the required modules in your code:
   ```python
   from tkinter import *
   from operaciones import Operaciones
   ```

3. Create an instance of the `Interfaz` class to display the graphical user interface:
   ```python
   ventana = Tk()
   app = Interfaz(ventana)
   ventana.mainloop()
   ```

4. Customize the `Operaciones` class by completing the necessary calculations based on your requirements.

5. Run your Python program to execute the logic and display the graphical user interface.

## Functionality

The `Interfaz` class creates a graphical user interface using the Tkinter library. It displays a window with labels and buttons for performing operations on a given number.

The `Operaciones` class contains methods that perform specific mathematical operations on a given number. The methods are used as commands for the buttons in the graphical user interface.

Feel free to explore and modify the code to meet your specific needs.

Note: Make sure to have Tkinter installed on your Python environment to run the graphical user interface successfully.

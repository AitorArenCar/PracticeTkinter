'''
Atención: No modificar este archivo.
Abrir el archivo operaciones.py y, de acuerdo a la consigna dada, completar únicamente donde aparecen comentarios indicados con #
Luego ejecutar este programa python.
'''


from tkinter import *
from operaciones import *

class Interfaz: 
    def __init__(self, ventana):
        self.ventana = ventana
        operaciones=Operaciones(self)
        self.superior=Frame(self.ventana)
        self.superior.pack(side=TOP)
        self.numero = Label(self.superior, text="número:\n16823", font=("Arial Bold", 17))
        self.numero.pack(padx=15, pady=45, side=LEFT)
        self.resultado = Label(self.superior, text="resultado: ", width=25, height=2, bg="white", font=("Arial", 12))
        self.resultado.pack(padx=15, pady=45, side=RIGHT)
        self.inferior=Frame(self.ventana)
        self.inferior.pack(side=TOP)
        self.btn1 = Button(self.inferior, text="Último\nDígito", bg="light blue", height=2, width=9, command=operaciones.ultimoDigito)
        self.btn2 = Button(self.inferior, text="Dos Últimos\nDígitos", bg="light blue", height=2, width=9, command=operaciones.dosUltimos)
        self.btn3 = Button(self.inferior, text="Tres Últimos\nDígitos", bg="light blue", height=2, width=9, command=operaciones.tresUltimos)
        self.btn4 = Button(self.inferior, text="Excepto el\nÚltimo", bg="light green", height=2, width=9, command=operaciones.exceptoUltimo)
        self.btn5 = Button(self.inferior, text="Primer\nDígito", bg="light green", height=2, width=9, command=operaciones.primerDigito)
        self.btn6 = Button(self.inferior, text="Primeros\nDos", bg="light green", height=2, width=9, command=operaciones.primerosDos)
        self.btn1.grid(column=0, row=1)
        self.btn2.grid(column=1, row=1)
        self.btn3.grid(column=2, row=1)
        self.btn4.grid(column=0, row=2)
        self.btn5.grid(column=1, row=2)
        self.btn6.grid(column=2, row=2)

def main(): 
    ventana = Tk()
    ventana.geometry('500x300')
    ventana.title("Desglosando un número...")
    app = Interfaz(ventana)
    ventana.mainloop()


if __name__ == '__main__':
    main()

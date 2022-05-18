from cgitb import text
from random import random
import qrcode
from tkinter import *


def crearQr():
    valor = entryText.get()
    qr = qrcode.make(valor)
    type(qr)
    namevalor = random()
    qr.save(f'{str(namevalor)}.png')
    print(qr)
    img = PhotoImage(file='./guardado.png')
    cuadroImagen= Label(root,image=img,bd = 0)
    cuadroImagen.grid(row=4,column=4)
    # mostrarQr()

def mostrarQr():
    img = PhotoImage(file='./guardado.png')
    cuadroImagen= Label(root,image=img,bd = 0)
    cuadroImagen.grid(row=4,column=4)

root = Tk()
root.config(bd=15)
root.title('createQr') 

textoBien = Label(text='Bienvenido al software para crear Qrs')
textoBien.grid(row=1,column=2)
entryText = Entry()
entryText.grid(row=1, column=1)
textoQr = Label(text="niam")
textoQr.grid(row=2 , column=1)
boton = Button(root , text = "CrearQR （＾∀＾●）ﾉｼ",command=crearQr)
boton.grid(row=3,column=1)

root.mainloop()
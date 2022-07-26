#conversor fahrenheit para Celsius

from cProfile import label
from tkinter import *
from tokenize import Double

def converter():
    F = float(textField_1.get())
    Celsius = (F-32) / 1.8
    Celsius_str = str(f'{Celsius:.2f}').replace('.',',')
    varTexto.set(Celsius_str + ' graus Celsius')


root = Tk()
window = Frame(root)

varTexto = StringVar()

root.geometry('125x120')
label_1 = Label(window,text ='Inserir Fahrenheit')
textField_1 = Entry(window)
label_2 = Label(window, textvariable = varTexto)
botao = Button(window,text='Calcular',command = converter)

label_1.grid()
textField_1.grid()
label_2.grid()
botao.grid()
window.grid()

root.mainloop()


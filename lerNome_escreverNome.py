from cProfile import label
from tkinter import *

# Lógica
def lerNome():
    texto = textField_1.get()
    label_2 = Label(root, text = 'O teu nome é: ' + texto)
    label_2.grid()

# Tela
root = Tk()
root.geometry('125x150')

# widgets
texto = StringVar()
label_1= Label(root,text='Digite seu nome: ')
textField_1 = Entry(root)
botao = Button(root, text='Ler',command = lerNome)

# exibir
label_1.grid()
textField_1.grid()
botao.grid()

root.mainloop()
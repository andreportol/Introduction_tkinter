from cProfile import label
from tkinter import *

def lerCampoUsuario():
    lb['text'] = campo_Usuario.get()


window = Tk()

campo_Usuario = Entry(window)
campo_Visor = Entry(window)
botao = Button(window,text='Executar',command = lerCampoUsuario)
lb = Label(window)

campo_Usuario.grid()
campo_Visor.grid()
botao.grid()
lb.grid()

campo_Usuario.focus()





window.mainloop()
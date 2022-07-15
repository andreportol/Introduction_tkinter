from tkinter import *

window = Tk()
window.geometry('450x150')                                                                    # sticky alinha a esquerda(oeste)
label_usuario = Label(window,text='Usuario: ',
                font='Ariel 15',
                anchor=CENTER,  
                padx=10,
                pady=5,
                justify=RIGHT).grid(row=0,column=0,sticky=W)
label_password = Label(window,text='Password: ',
                font='Ariel 15',
                anchor=CENTER,  
                padx=10,
                pady=5,
                justify=RIGHT).grid(row=1,column=0,sticky=W)

text_usuario = Entry(window,background='white',bd=9,border=5,relief="groove")
text_usuario.grid(row=0,column=1,sticky=W,)
text_password = Entry(window)
text_password.grid(row=1,column=1,sticky=W)

# a tecla tab quando pressionada 
# faz com que o ponteiro siga a 
# sequencia da chamada do metodo grid
text_usuario.focus() # para abrir a tela com o focus


window.mainloop()
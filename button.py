from tkinter import *


window = Tk() 
window.title('GFAI')                      
window.geometry("500x250+200+200")  
# Metodo
def event_click(novaMensagem):
    print(novaMensagem)

#botao
btn =Button(window,text='Botao 1',command=lambda:event_click('Mensagem'))
btn1 =Button(window,text='Botao 2',command=lambda:print('Nova Mensagem'))
btn.pack()
btn1.pack()

window.mainloop()
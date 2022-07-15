from tkinter import *

from setuptools import Command

# método chamado pela funçao lambda durante a criaçao do btn
def cmd_click(mensagem):
    print(mensagem)

# Janela
window = Tk() # objeto window
window.title('GFAI') # chamando o método title
                        # 200 e 200 posiçao inicial da tela 200 pixes para x e 200 pixes para y
window.geometry("500x250+200+200")  #tamanho inicial da tela(largura, altura)
window.resizable(True,True) # a janela não pode ser aumentada com False para x e y
#window.minsize(width=500,height=250)
#window.maxsize(1000,900)
#window.state("zoomed") # tela maximizada
window.iconbitmap('img/icon_gremio.ico')


# botao   btn é uma instancia de Button      #cmd_click é um método
btn = Button(window, text="Pesquisar",command=lambda:cmd_click("Nova mensagem")) # botao pertence a janela window
btn.pack() # aparecer o botao

btn1 = Button(window, text="Inserir",command= lambda: print('inserir')) # botao pertence a janela window
btn1.pack() # aparecer o botao


# Label
border = 4
label_1 = Label(window, text="solid",
                #bg="red",
                font="Ariel 10",
                borderwidth= border,
                relief="solid",
                width=20) # largura do background
label_1.pack() # aparecer o label
#label_2 = Label(window, text="Este é o label 2.")
#label_2.pack() # aparecer o label

label_2 = Label(window, text="groove",
                font="Ariel 10",
                borderwidth= border,
                relief="groove",
                width=20)
label_2.pack()
label_3 = Label(window, text="flat",
                font="Ariel 10",
                borderwidth= border,
                relief="flat",
                width=20)
label_3.pack()
label_4 = Label(window, text="raised",
                font="Ariel 10",
                borderwidth= border,
                relief="raised",
                width=20)
label_4.pack()
label_5 = Label(window, text="sunken",
                font="Ariel 10",
                borderwidth= border,
                relief="sunken",
                width=20)
label_5.pack()
label_6 = Label(window, text="ridge",
                font="Ariel 10",
                borderwidth= border,
                relief="ridge",
                width=20)
label_6.pack()



window.mainloop()

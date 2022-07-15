from tkinter import *

# Janela
window = Tk() # objeto window
window.title('GFAI') # chamando o método title
                        # 200 e 200 posiçao inicial da tela 200 pixes para x e 200 pixes para y
window.geometry("500x250")  #tamanho inicial da tela(largura, altura)
window.resizable(True,True) # a janela não pode ser aumentada com False para x e y
#window.minsize(width=500,height=250)
#window.maxsize(1000,900)
#window.state("zoomed") # tela maximizada

# GRID
label1= Label(window,text='label 1',font='Ariel 20',bg='red' )
label2= Label(window,text='label 2',font='Ariel 20',bg='green' )
label3= Label(window,text='label 3',font='Ariel 20',bg='blue' )
label1.grid(row=0,column=0)
label2.grid(row=1,column=1)
label3.grid(row=2,column=2)

label4= Label(window,text='label 4',font='Ariel 20',bg='red' )
label5= Label(window,text='label 5',font='Ariel 20',bg='green' )
label6= Label(window,text='label 6',font='Ariel 20',bg='blue' )
label4.grid(row=3,column=0)
label5.grid(row=3,column=1)
label6.grid(row=3,column=2)

btn1 = Button(window,text= "botao 1")
btn2 = Button(window,text= "botao 2")
btn3 = Button(window,text= "botao 3")
btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)

window.mainloop()
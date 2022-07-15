from tkinter import *

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
window.mainloop()
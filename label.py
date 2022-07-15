from tkinter import *


window = Tk() 
window.title('GFAI')                      
window.geometry("500x250+200+200")

# Label
# Label
border = 4
label_1 = Label(window, text="solid",
                #bg="red",
                font="Ariel 10",
                borderwidth= border,
                relief="solid",
                width=20, # largura do background onde aparecerá o label
                height = 2, # significa o número de text que se pode colocar dentro do width(alinhados pela coluna)
                anchor=CENTER,  # alinhamento do texto dentro do width
                padx=10,
                pady=5,
                justify=RIGHT) # alinhamento do texto considerando o proprio texto

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

label_7 = Label(window,text='text label 7')

label_7['font'] = "Arial 20"
label_7['bd'] = 1
label_7['relief'] = 'solid'
label_7.pack()

label_7['text'] = 'Novo texto do label 7'

texto = StringVar()
texto.set('André Porto')
label_8 = Label(window,
                font="Arial 20",
                bg='red',
                fg='white',
                textvariable=texto)

label_8.pack()
texto.set('André Luzardo Porto')
window.mainloop()
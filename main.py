from tkinter import *
from tkinter import ttk

# cores

cor1 = "#3b3b3b" # black
cor2 = "#feffff" # white
cor3 = "#38576b" # blue
cor4 = "#ECEFF1" # gray
cor5 = "#FFAB40" # orange

janela = Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=300, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=300, height=350)
frame_corpo.grid(row=1, column=0)

janela.mainloop()

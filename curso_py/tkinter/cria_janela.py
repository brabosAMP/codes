from tkinter import *

janela = Tk()
janela.title('Curso de Python')
janela.geometry('500x500')
janela.resizable(True, True)

Label(janela, text = 'Hello World!', bg='orange', fg='black', padx=30, pady=30).grid(row=0, column=0)


janela.mainloop()


import tkinter as tk
from typing import List

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=10, pady=10, bg='#fff')
    root.resizable(False, False)
    return root

def make_label(root) -> tk.Label:
    label = tk.Label(root, text='Sem conta', anchor='e', justify='right', bg='#fff')
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0,10))
    display.config(font=('Helvetica',40,'bold'), 
                   justify='right', bd=1, relief='flat', 
                   highlightthickness=1, 
                   highlightcolor='#ccc'
                   )
    display.bind('<Control-a>', display_ctrl_a) #evento
    return display

def display_ctrl_a(event):
    event.widget.select_range(0,'end')
    event.widget.icursor('end')
    return 'break'

def make_botoes(root) -> List[List[tk.Button]]:
    botoes_textos: List[List[str]] = [
        ['7','8','9','+','C'],
        ['4','5','6','-','/'],
        ['1','2','3','*','^'],
        ['0','.','(',')','=']
    ]

    botoes: List[List[tk.Button]] = []

    for row_index, row_value in enumerate(botoes_textos, start=2):
        botao_row = []
        for column_index, coumn_value in enumerate(row_value):
            botao = tk.Button(root, text=coumn_value)
            botao.grid(row=row_index, column=column_index, sticky='news', padx=5, pady=5)
            botao.config(font=('Helvetica', 15, 'normal'), 
                         pady=25, width=1, bg='#87788f', 
                         bd=0, cursor='hand2', 
                         highlightthickness=1, highlightcolor='#ccc', 
                         highlightbackground='#ccc', activebackground='#ccc'
                         )
            botao_row.append(botao)
        botoes.append(botao_row)

    return botoes
from tkinter import *
from tkinter import ttk

#cores
fundo = '#000000'
cor_display = '#2c323b'
cor_botoes = '#7c818a'
cor_operacoes = '#d48415'
cor_numeros = '#ffffff'

#criando a janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=fundo)
janela.resizable(width=False, height='False')

#dividindo a janela
frame_display = Frame(janela, width=235, height=50, bg=cor_display)
frame_display.grid(row=0,column=0)
frame_teclado = Frame(janela, width=235,height=268)
frame_teclado.grid(row=1, column=0)

#variável de controle
todos_valores = ''

#função para receber valores
def entrar_valores(valor):
    global todos_valores

    todos_valores = todos_valores + str(valor)
    valor_texto.set(todos_valores)

#fução de cálculo
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#criando o label para o display
valor_texto = StringVar()
display_label = Label(frame_display, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'),bg = cor_display, fg=cor_numeros)
display_label.place(x=0,y=0)

#criando os botões

#linha 1
botao_clear = Button(frame_teclado, command=limpar_tela, text='C', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_operacoes)
botao_clear.place(x=0,y=0)
botao_modulo = Button(frame_teclado, command=lambda:entrar_valores('%'), text='%', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_operacoes)
botao_modulo.place(x=118,y=0)
botao_divisao = Button(frame_teclado, command=lambda:entrar_valores('/'), text='/', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_operacoes)
botao_divisao.place(x=177,y=0)

#linha 2
botao_7 = Button(frame_teclado, command=lambda:entrar_valores('7'), text='7', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes )
botao_7.place(x=0,y=52)
botao_8 = Button(frame_teclado, command=lambda:entrar_valores('8'), text='8', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes)
botao_8.place(x=59,y=52)
botao_9 = Button(frame_teclado, command=lambda:entrar_valores('9'), text='9', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes)
botao_9.place(x=118,y=52)
botao_x = Button(frame_teclado, command=lambda:entrar_valores('*'), text='*', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_operacoes)
botao_x.place(x=177,y=52)

#linha 3
botao_4 = Button(frame_teclado, command=lambda:entrar_valores('4'), text='4', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes )
botao_4.place(x=0,y=104)
botao_5 = Button(frame_teclado, command=lambda:entrar_valores('5'), text='5', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes)
botao_5.place(x=59,y=104)
botao_6 = Button(frame_teclado, command=lambda:entrar_valores('6'), text='6', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes)
botao_6.place(x=118,y=104)
botao_menos = Button(frame_teclado, command=lambda:entrar_valores('-'), text='-', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_operacoes)
botao_menos.place(x=177,y=104)

#linha 4
botao_1 = Button(frame_teclado, command=lambda:entrar_valores('1'), text='1', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes )
botao_1.place(x=0,y=156)
botao_2 = Button(frame_teclado, command=lambda:entrar_valores('2'), text='2', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes)
botao_2.place(x=59,y=156)
botao_3 = Button(frame_teclado, command=lambda:entrar_valores('3'), text='3', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes)
botao_3.place(x=118,y=156)
botao_mais = Button(frame_teclado, command=lambda:entrar_valores('+'), text='+', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_operacoes)
botao_mais.place(x=177,y=156)

#linha 5
botao_0 = Button(frame_teclado, command=lambda:entrar_valores('0'), text='0', width=11, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes)
botao_0.place(x=0,y=208)
botao_ponto = Button(frame_teclado, command=lambda:entrar_valores('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_botoes )
botao_ponto.place(x=118,y=208)
botao_igual = Button(frame_teclado, command=calcular, text='=', width=5, height=2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,bg=cor_operacoes)
botao_igual.place(x=177,y=208)

janela.mainloop()
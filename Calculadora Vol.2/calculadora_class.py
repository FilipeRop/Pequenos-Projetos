import tkinter as tk
import re
import math
from typing import List

class Calculadora:
    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry, botoes: List[List[tk.Button]]):
        self.root = root
        self.label = label
        self.display = display
        self.botoes = botoes


    def start(self):
        self.config_botoes()
        self.config_display()
        self.root.mainloop()
    
    def config_botoes(self):
        botoes = self.botoes
        for row_values in botoes:
            for botao in row_values:
                botao_texto = botao['text']

                if botao_texto == 'C':
                    botao.bind('<Button-1>', self.clear)
                    botao.config(bg='orange', fg='#fff')

                if botao_texto in '0123456789.+-/*()^':
                    botao.bind('<Button-1>', self.add_display)

                if botao_texto == '=':
                    botao.bind('<Button-1>', self.calcular)
                    botao.config(bg='blue', fg='#fff')


    def config_display(self):
        self.display.bind('<Return>', self.calcular)
        self.display.bind('<KP_Enter>', self.calcular)

    def texto_corrigido(self, text):
        #substituição de itens
        text = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', text, 0)
        text = re.sub(r'([\.\+\/\-\*\^])\1+', r'\1', text, 0)
        text = re.sub(r'\*?\(\)', '', text)

        return text

    def clear(self, event=None):
        self.display.delete(0, 'end')
    
    def add_display(self, event=None):
        self.display.insert('end', event.widget['text'])
    
    def calcular(self, event=None):
        texto_corrigido = self.texto_corrigido(self.display.get())
        equacao = self.get_equacoes(texto_corrigido)
        try: 
            if len(equacao) == 1:
                resultado = eval(self.texto_corrigido(equacao[0]))
            else:
                resultado = eval(self.texto_corrigido(equacao[0]))
                for i in equacao[1:]:
                    resultado = math.pow(resultado, eval(self.texto_corrigido(i)))

            self.display.delete(0,'end')
            self.display.insert('end', resultado)
            self.label.config(text=f'{texto_corrigido} = {resultado}')

        except OverflowError:
            self.label.config(text='Não foi possível realizar o cálculo.')
        except Exception:
            self.label.config(text='Operação Inválida.')
    
    def get_equacoes(self, text):
        return re.split('\^', text, 0)
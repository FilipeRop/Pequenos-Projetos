from calculadora_maker import make_root, make_label, make_display, make_botoes
from calculadora_class import Calculadora

def main():
    root = make_root()
    label = make_label(root)
    display = make_display(root)
    botoes = make_botoes(root)
    calculadora =  Calculadora(root, label, display, botoes)
    calculadora.start()
    
if __name__ == '__main__':
    main()
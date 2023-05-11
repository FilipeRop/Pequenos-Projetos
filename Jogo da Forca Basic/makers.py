import random 
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_hangman(chances):

    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def game():
    limpa_tela()
    print('\nBem-vindo ao jogo da forca!')
    print('Advinhe a palavra abaixo:\n')

    chances = 6
    letras_erradas = []
    
    palavras = ['manga', 'uva', 'laranja', 'morango', 'kiwi', 'goiaba']
    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    while chances > 0:
        print(display_hangman(chances))
        print(''.join(letras_descobertas))
        print(f'\nChances restantes: {chances}')
        print('Letras erradas: ',' '.join(letras_erradas))

        tentativa = input('\nEscreva uma letra: ').lower()

        if tentativa in palavra:
            i = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[i] = letra
                i+=1
        else:
            chances-= 1
            letras_erradas.append(tentativa)

        if '_' not in letras_descobertas:
            print(f'\nVocê venceu, a palavra era: {palavra}.')
            break
    if '_' in letras_descobertas:
        print(f'\nVocê perdeu. A palavra era: {palavra}')

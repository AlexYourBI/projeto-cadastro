import os
import time
import sys
from tabulate import tabulate
from tqdm import tqdm
import random
from colorama import Fore, Style
import keyboard
import webbrowser
from db_connection import apaga_csv,exportar_para_csv, criar_tabelas
#abertura do sistema com abresentação do gato e a barra de carregamento

#---------------

palavras = ['alex', 'python', 'fiap','leo','joao','minas','gabriel', 'zl']

def barra():
    # Função para imprimir a barra de carregamento
    def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
        sys.stdout.flush()  # Forçar a exibição da barra de progresso na tela

    # Configurações da barra de carregamento
    total_steps = 10
    bar_length = 50
    
    for i in range(total_steps):
        print_progress_bar(i + 1, total_steps, prefix='Progresso:', suffix='Completo', length=bar_length)
        time.sleep(0.5)  # Simula o tempo de espera entre cada etapa 

def gato():
    print('\nIniciando abertura do APP de SGV...')
    color = random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA])
    print(color + '''

───▄▄─▄████▄▐▄▄▄▌
──▐──████▀███▄█▄▌
▐─▌──█▀▌──▐▀▌▀█▀
─▀───▌─▌──▐─▌
─────█─█──▐▌█

''' + Style.RESET_ALL)  # Imprime o texto com a cor selecionada
   
def msg_abertura():
    print("\nAbertura do Sistema de Cadstro SGV concluída!")
    time.sleep(0.5)

def nome_app():
    color = random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA])
    print(color +'''
█▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▀▄ █▀▀   █▀█ █▀█ █▀█ █▀▄ █░█ ▀█▀ █▀█ █▀   █▀ █▀▀ █░█
█▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█   █▄▀ ██▄   █▀▀ █▀▄ █▄█ █▄▀ █▄█ ░█░ █▄█ ▄█   ▄█ █▄█ ▀▄▀ 
''' 
+ Style.RESET_ALL)  # Imprime o texto com a cor selecionada

def nome_grupo():
    color = random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA])
    print(color +''' 


        ▀█ █▀█ █▄░█ ▄▀█   █░░ █▀▀ █▀ ▀█▀ █▀▀   ▄▄ █▀▄▀█ █▀▀
        █▄ █▄█ █░▀█ █▀█   █▄▄ ██▄ ▄█ ░█░ ██▄   ░░ █░▀░█ █▄█   
                          
        '''+ Style.RESET_ALL)  # Imprime o texto com a cor selecionada    
  
def joia():
    color = random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA])
    print(color +'''
  
            ░░░░░░░░░░░░░░░░░░░█████████
            ░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
            ░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
            ░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
            ░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
            ░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
            ░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
            ░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
            ░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
            ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
            █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
            ░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
            ░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
            ░░████████████░░░█████████████████
 
                  '''+ Style.RESET_ALL)  # Imprime o texto com a cor selecionada 
    
def baleia():
    color = random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA])
    print(color +
          '''
▄██████████████▄▐█▄▄▄▄█▌
██████▌▄▌▄▐▐▌███▌▀▀██▀▀
████▄█▌▄▌▄▐▐▌▀███▄▄█▌
▄▄▄▄▄██████████████▀

''' 
+ Style.RESET_ALL)  # Imprime o texto com a cor selecionada
 
def imagem_caca_palavra():
    color = random.choice([Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA])
    print(color +
        '''          
P	Y	T	H	O	N	S					A
                            Q				U
M	E	S	E	R	A	V	I	L			G
Z	O	N	A	L	E	S	T	E	M	G	U
                C	J	O	Ã	O			S
                H				N			T
F			    A				A			O
    I		T	G	A	B	R	I	E	L
        A	G		L		D			
            P		E		O			
            T		X					
D	A	T	A	S	C	I	E	N	C	E	

  ALEX     AUGUSTO   CHATGPT   DATASCIENCE   
  FIAP     GABRIEL    JOÃO      LEONARDO
MESERAVI   PYTHON      SQL     ZONALESTEMG
                  '''+ Style.RESET_ALL)  # Imprime o texto com a cor selecionada 
   
def escolher_palavra():
    return random.choice(palavras)

def jogar():
    palavra = escolher_palavra()
    letras_erradas = ''
    letras_corretas = ''
    tentativas = 6
    desenho_bonequinho = [
        """
           +---+
               |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """
    ]

    while True:
        # Mostra o estado atual da palavra
        palavra_secreta = ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_secreta += letra
            else:
                palavra_secreta += '_'
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Palavra:', palavra_secreta)
        print('Tentativas restantes:', tentativas)
        print('Letras erradas:', letras_erradas)

        # Mostra o desenho do bonequinho correspondente às tentativas restantes
        print(desenho_bonequinho[6 - tentativas])

        # Verifica se o jogador venceu
        if '_' not in palavra_secreta:
            input()
            print('Parabéns! Você venceu!')
            break
            
        # Verifica se o jogador perdeu
        if tentativas == 0:
            input()
            print('Game over! A palavra era:', palavra)
            break
        # Solicita uma letra ao jogador
        letra = input('Digite uma letra: ').lower()

        # Verifica se a letra já foi escolhida antes
        if letra in letras_corretas or letra in letras_erradas:
            print('Você já escolheu esta letra. Tente novamente.')
            continue

        # Verifica se a letra está na palavra
        if letra in palavra:
            letras_corretas += letra
        else:
            letras_erradas += letra
            tentativas -= 1

def caca_palavra():
    try:
        tempo_em_segundos = int(input("Informe o tempo em segundos: "))
       
        contador_tempo(tempo_em_segundos)
           
    except ValueError:
        print("Por favor, insira um número válido.")

def contador_tempo(segundos):
    imagem_caca_palavra()  
    for i in tqdm(range(segundos), desc="Tempo restante", unit="seg"):
        time.sleep(1)
    print("Tempo esgotado!")

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela

    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def link():



    
    #print("https://www.linkedin.com/in/alexlourenc/")
   
    #webbrowser.open("https://www.linkedin.com/in/alexlourenc/")
    
    keyboard.wait("enter")

    url()
    
def url(): 
    webbrowser.open("https://www.linkedin.com/in/alexlourenc/")

    exit()

#---------------------------------------------------------------------------------------------------------

def abertura():
    gato()
    barra()
    criar_tabelas()
    msg_abertura()

def finalizar():
    apaga_csv()
    exportar_para_csv()
    os.system('Cls')
    nome_grupo()
    time.sleep(2) 
    joia()
    time.sleep(2) 
    os.system('Cls')
    
    
   # print('Bem vindo ao BONUS... \n')  
   
   # opcoes = [1,2,3 ]
   # opcao_escolhida = random.choice(opcoes)

   # if opcao_escolhida == 1:
             
   #    caca_palavra ()  
                    
   # elif opcao_escolhida== 2:
   #    jogar()
                
    
    
    os.system('Cls')
    print('''Obrigado por utilizar nosso APP...
                  
                  ''')        
            
    exit()

   
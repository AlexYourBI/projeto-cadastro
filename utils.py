import os
import time
import sys
from tabulate import tabulate
from tqdm import tqdm
import random
from colorama import Fore, Style
from db_connection import apaga_csv,exportar_para_csv, criar_tabelas
#abertura do sistema com abresentação do gato e a barra de carregamento

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
    print('''Obrigado por utilizar nosso APP...
                  
                  ''')        
            
    exit()

   
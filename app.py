import sqlite3
import os
from tabulate import tabulate
from colorama import Fore, Style
import csv
import time
import sys
from tqdm import tqdm
import random

contador = 0

# Função para criar as tabelas se ainda não existirem no banco de dados
def criar_tabelas():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS TB_EMBALAGEM (
                        CD_EMBALAGEM INTEGER PRIMARY KEY,
                        DS_EMBALAGEM TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS TB_CATEGORIA (
                        CD_CATEGORIA INTEGER PRIMARY KEY,
                        DS_CATEGORIA TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS TB_PRODUTO (
                        CD_PRODUTO INTEGER PRIMARY KEY,
                        CD_EMBALAGEM INTEGER,
                        CD_CATEGORIA INTEGER,
                        DS_PRODUTO TEXT,
                        VL_PRECO REAL,
                        FOREIGN KEY(CD_CATEGORIA) REFERENCES TB_CATEGORIA(CD_CATEGORIA))''')
    
    conexao.commit()
    conexao.close()
   
    # Exportar dados para CSV

def exportar_para_csv():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()

    # Consulta SQL para recuperar os dados das tabelas
    cursor.execute('''SELECT * FROM TB_EMBALAGEM''')
    embalagens = cursor.fetchall()

    cursor.execute('''SELECT * FROM TB_CATEGORIA''')
    categorias = cursor.fetchall()

    cursor.execute('''SELECT * FROM TB_PRODUTO''')
    produtos = cursor.fetchall()

    # Exportar dados para o arquivo CSV
    with open('embalagens.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['CD_EMBALAGEM', 'DS_EMBALAGEM'])
        escritor_csv.writerows(embalagens)

    with open('categorias.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['CD_CATEGORIA', 'DS_CATEGORIA'])
        escritor_csv.writerows(categorias)

    with open('produtos.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['CD_PRODUTO', 'CD_EMBALAGEM','CD_CATEGORIA', 'DS_PRODUTO', 'VL_PRECO'])
        escritor_csv.writerows(produtos)

    conexao.close()
    # Verifica se os arquivos CSV já existem e, se sim, os exclui

def apaga_csv():
    if os.path.exists('embalagens.csv'):
        os.remove('embalagens.csv')

    if os.path.exists('categorias.csv'):
        os.remove('categorias.csv')

    if os.path.exists('produtos.csv'):
        os.remove('produtos.csv')
     
#--------------------------------------------------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------------

# Função para inserir uma nova embalagem
def inserir_embalagem():
    exibir_subtitulo('Cadastrar embalagem')
    listar_embalagens()
    while True:
        descricao = input("Digite a descrição da embalagem: ").strip().upper()  # Remova espaços em branco e converta para maiúsculas
        if descricao:  # Verifica se a descrição não está vazia
            break
        else:
            input("Descrição não pode ser em branco. Por favor, tente novamente.")
            inserir_embalagem()

    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO TB_EMBALAGEM (DS_EMBALAGEM) VALUES (?)", (descricao,))
    conexao.commit()
    conexao.close()
    listar_embalagens()
    menu_crud_embalagem()

# Função para inserir uma nova categoria
def inserir_categoria():
    exibir_subtitulo('Cadastrar categoria')
    listar_categorias()
    while True:
        descricao = input("Digite a descrição da categoria: ").strip().upper()  # Remova espaços em branco e converta para maiúsculas
        if descricao:  # Verifica se a descrição não está vazia
            break
        else:
            input("Descrição não pode ser em branco. Por favor, tente novamente.")
            inserir_categoria()

    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO TB_CATEGORIA (DS_CATEGORIA) VALUES (?)", (descricao,))
    conexao.commit()
    conexao.close()
    listar_categorias()
    menu_crud_categoria()

# Função para listar embalagens para excluir
def listar_embalagens_sem_vinculo():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT c.CD_EMBALAGEM, c.DS_EMBALAGEM FROM TB_EMBALAGEM c LEFT JOIN TB_PRODUTO p ON c.CD_EMBALAGEM = p.CD_EMBALAGEM WHERE p.CD_EMBALAGEM IS NULL")
    embalagens = cursor.fetchall()
    conexao.close()
    
    exibir_subtitulo('Lista embalagens sem vículo')
    headers = ["ID", "Embalagem"]
    tabela_produtos = []
    for embalagem in embalagens:
        tabela_produtos.append(embalagem)

    print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))

# Função para listar categorias para excluir
def listar_categorias_sem_vinculo():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT c.CD_CATEGORIA, c.DS_CATEGORIA FROM TB_CATEGORIA c LEFT JOIN TB_PRODUTO p ON c.CD_CATEGORIA = p.CD_CATEGORIA WHERE p.CD_CATEGORIA IS NULL")
    categorias = cursor.fetchall()
    conexao.close()
    
    exibir_subtitulo('Lista Categorias sem vículo')
    headers = ["ID", "Categoria"]
    tabela_produtos = []
    for categoria in categorias:
        tabela_produtos.append(categoria)

    print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))

# Função para excluir uma embalagem
def excluir_embalagem():
    listar_embalagens_sem_vinculo() 
    try:
        cd_embalagem = input("Digite o [ID] da embalagem que deseja excluir: ")
        conexao = sqlite3.connect('cadastro_produtos.db')
        cursor = conexao.cursor()

        # Verificar se a embalagem tem produtos vinculados
        cursor.execute("SELECT COUNT(*) FROM TB_PRODUTO WHERE CD_EMBALAGEM = ?", (cd_embalagem,))
        total_produtos = cursor.fetchone()[0]

        if total_produtos > 0:
            print("Esta embalagem possui produtos vinculados e não pode ser excluída.")
            baleia()
        else:
            # Excluir a embalagem
            cursor.execute("DELETE FROM TB_EMBALAGEM WHERE CD_EMBALAGEM = ?", (cd_embalagem,))
            conexao.commit()
            print("Embalagem excluída com sucesso.")
            listar_embalagens()
        conexao.close()
        
    except sqlite3.Error as e:
        print("Erro ao excluir a embalagem:", e)

# Função para excluir uma categoria
def excluir_categoria():
    listar_categorias_sem_vinculo() 
    try:
        cd_categoria = input("Digite o [ID] da categoria que deseja excluir: ")
        conexao = sqlite3.connect('cadastro_produtos.db')
        cursor = conexao.cursor()

        # Verificar se a categoria tem produtos vinculados
        cursor.execute("SELECT COUNT(*) FROM TB_PRODUTO WHERE CD_CATEGORIA = ?", (cd_categoria,))
        total_produtos = cursor.fetchone()[0]

        if total_produtos > 0:
            print("Esta categoria possui produtos vinculados e não pode ser excluída.")
            baleia()
        else:
            # Excluir a categoria
            cursor.execute("DELETE FROM TB_CATEGORIA WHERE CD_CATEGORIA = ?", (cd_categoria,))
            conexao.commit()
            print("Categoria excluída com sucesso.")
            listar_categorias()
        conexao.close()

    except sqlite3.Error as e:
        print("Erro ao excluir a categoria:", e)
  
# verifica categoria
def verificar_categoria_existente(cd_categoria):
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM TB_CATEGORIA WHERE CD_CATEGORIA = ?", (cd_categoria,))
    resultado = cursor.fetchone()[0]
    conexao.close()
    return resultado > 0

# verifica embalagem
def verificar_embalagem_existente(cd_embalagem):
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM TB_EMBALAGEM WHERE CD_EMBALAGEM = ?", (cd_embalagem,))
    resultado = cursor.fetchone()[0]
    conexao.close()
    return resultado > 0

# Função para inserir um novo produto
def inserir_produto():
    
    exibir_subtitulo('Cadastro de novos produtos')
    
    listar_categorias()

    cd_categoria = input("Por favor, insira o [ID] correspondente à categoria do produto que você pretende cadastrar: ")
     
    if not verificar_categoria_existente(cd_categoria):
        exibir_subtitulo('Cadastro de novos produtos')
    
        print("\n\033[33m Que pena!!! O ID que você informou não foi localizado, gostaria de cadastrar uma nova categoria? \033[0m") 
        baleia()
        menu_opcao_cadastro(1)
    #listar_categorias_cadastro(cd_categoria)

    ds_categoria = obter_descricao_categoria(cd_categoria)
    
    while True:
        exibir_subtitulo('Cadastro de novos produtos')
        descricao = input(f"[ {ds_categoria} ]\nPor favor, digite a descrição do produto: ").strip().upper()  # Remova espaços em branco e converta para maiúsculas
        if descricao:  # Verifica se a descrição não está vazia
            break
        else:
            input("Descrição não pode ser em branco. Por favor, tente novamente.")
           

    while True:
        exibir_subtitulo('Cadastro de novos produtos')

        try:
            preco_input = input(f"[ {ds_categoria} ] [ {descricao} ]\nInforme o preço do produto : ")
            preco_input = preco_input.replace(',', '.')  # Substitui ',' por '.'
            preco = float(preco_input)
            break
        except ValueError:
            input("Erro: O preço do produto deve ser um número. Por favor, tente novamente.")

    exibir_subtitulo('Cadastro de novos produtos')
    print (f'[ {ds_categoria} ] [ {descricao} ] [{preco}]')
   
    listar_embalagens()
        
    cd_embalagem = input("Por favor, insira o [ID] correspondente à embalagem do produto que você pretende cadastrar: ")
     
    if not verificar_embalagem_existente(cd_embalagem):
        exibir_subtitulo('Cadastro de novos produtos')
    
        print("\n\033[33m Que pena!!! O ID que você informou não foi localizado, gostaria de cadastrar uma nova embalagem? \033[0m") 
        baleia()
        menu_opcao_cadastro(2)
    #listar_categorias_cadastro(cd_categoria)


    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO TB_PRODUTO (CD_EMBALAGEM,CD_CATEGORIA, DS_PRODUTO, VL_PRECO) VALUES (?, ?, ? , ?)", (cd_embalagem,cd_categoria, descricao, preco))
    conexao.commit()
    conexao.close()
    listar_produtos()

def obter_descricao_categoria(cd_categoria):
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT DS_CATEGORIA FROM TB_CATEGORIA WHERE CD_CATEGORIA = ?", (cd_categoria,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return resultado[0]
    else:
        return None

# Função para listar embalagens
def listar_embalagens():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM TB_EMBALAGEM")
    embalagens = cursor.fetchall()
    conexao.close()
    
    exibir_subtitulo('Cadastro de Embalagens')
    headers = ["ID", "Embalagem"]
    tabela_produtos = []
    for embalagem in embalagens:
        tabela_produtos.append(embalagem)

    print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))
    
# Função para listar categorias
def listar_categorias():
    
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM TB_CATEGORIA")
    categorias = cursor.fetchall()
    conexao.close()
    
    exibir_subtitulo('Lista de Categorias')


    headers = ["ID", "Categoria"]
    tabela_produtos = []
    for categoria in categorias:
        tabela_produtos.append(categoria)

    print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))


    #menu_crud_categoria()
        
def listar_produtos():
    
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT p.CD_PRODUTO,  c.DS_CATEGORIA, p.DS_PRODUTO, p.VL_PRECO, e.DS_EMBALAGEM FROM TB_PRODUTO p inner join TB_CATEGORIA c on p.CD_CATEGORIA = c.CD_CATEGORIA inner join TB_EMBALAGEM e on p.CD_EMBALAGEM = e.CD_EMBALAGEM" )
    produtos = cursor.fetchall()
    conexao.close()
    
    exibir_subtitulo('Lista de produtos')
   
    headers = ["ID","Categoria", "Produto", "Preço", "Embalagem"]
    tabela_produtos = []

    for produto in produtos:
       
        produto = list(produto)
        preco = "{:.2f}".format(produto[3])  
        if '.' not in preco:  
            preco += '.00'  
        produto[3] = preco
        tabela_produtos.append(produto)
    
    print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))
    #menu_crud_produto()

   
    #voltar_ao_menu_principal()
 
# Função para excluir um produto
def excluir_produto():

    listar_produtos()
   
    cd_produto = input("Digite insira o [ID] do produto que deseja excluir: ")
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM TB_PRODUTO WHERE CD_PRODUTO = ?", (cd_produto,))
    conexao.commit()
    conexao.close()
    print("Produto excluído com sucesso.")
    listar_produtos()
    
def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal

    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

# Menu CRUD_produto
def menu_crud_produto():
 
    while True:
        
        print("\n1. Novo")
        print("2. Excluir")
        print('3. Voltar')
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            inserir_produto()      
        elif opcao == '2':
            excluir_produto()
        else:
            main()

# Menu CRUD_categoria
def menu_crud_categoria():  
    while True:
        
        print("\n1. Novo")
        print("2. Excluir")
        print('3. Voltar')
        opcao = input("\nEscolha uma opção: ")
        if opcao == '1':
            inserir_categoria() 
                
        elif opcao == '2':
            listar_categorias_sem_vinculo()
            excluir_categoria()

        else:
            main()

# Menu CRUD_embalagem
def menu_crud_embalagem():  
    while True:
        
        print("\n1. Novo")
        print("2. Excluir")
        print('3. Voltar')
        opcao = input("\nEscolha uma opção: ")
        if opcao == '1':
            inserir_embalagem()
            #voltar_ao_menu_principal()      
        elif opcao == '2':
            listar_embalagens_sem_vinculo()
            excluir_embalagem()

        else:
            main()

# Menu principal
def menu_principal():
    while True:
        print("Menu Principal:\n")
        print("1. Produto")
        print("2. Categoria")
        print("3. Embalagem")
        print("4. Finalizar Sistema")
        opcao = input("\nEscolha uma opção: ")
    
        if opcao == '1':
            listar_produtos()
            menu_crud_produto()
        elif opcao == '2':
            listar_categorias()
            menu_crud_categoria()
        elif opcao == '3':
            listar_embalagens()
            menu_crud_embalagem()
        elif opcao == '4':
            # Chame a função para obter o número de cadastros

            quantidade_cadastros = contar_cadastros()
            if quantidade_cadastros >=5 :
                finalizar() 
            else:
                 
                print("\nPara concluir, precisaremos que você cadastre pelo menos 5 produtos. Vamos lá?" )
                baleia()
                input()
                main()
        else:
            voltar_ao_menu_principal()
            print("Opção inválida. Tente novamente.")

# Menu opcao cadastro
def menu_opcao_cadastro(parametro):
    while True:
        if parametro == 1:
            print("1. Cadastrar nova Categoria ")
            print("2. Voltar")
            opcao = input("\nEscolha uma opção: ")
            if opcao == '1':
                inserir_categoria()
            else:
                listar_produtos()
                menu_crud_produto()
        elif parametro == 2:
            print("1. Cadastrar Embalagem ")
            print("2. Voltar")
            opcao = input("\nEscolha uma opção: ")
            if opcao == '1':
                    inserir_embalagem()
                    
            else:
                listar_produtos()
                menu_crud_produto()
        else:
            print("Parâmetro inválido.")

def contar_cadastros():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM TB_PRODUTO")
    quantidade = cursor.fetchone()[0]  # Captura o resultado da contagem
    conexao.close()
    return quantidade

# Função principal

def main():
    global contador  # Indica que a variável contador é global
    contador += 1    # Incrementa o contador em 1
    if contador == 1 :
        abertura() 
        
    os.system('cls')
    nome_app()
    #criar_tabelas()
    # Chame a função para obter o número de cadastros
    quantidade_cadastros = contar_cadastros()
    print("Número total de cadastros:", quantidade_cadastros,'\n')

    menu_principal()

if __name__ == "__main__":
    main()
    

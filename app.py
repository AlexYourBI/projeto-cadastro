import sqlite3
import csv
import os
import time
import sys
from tabulate import tabulate
from tqdm import tqdm
import tkinter as tk
import random
from colorama import Fore, Style
from utils import baleia,joia,jogar,nome_grupo,caca_palavra,abertura,exibir_subtitulo,exibir_nome_do_programa
from db_connection import criar_tabelas,exportar_para_csv,apaga_csv
import pyperclip



contador = 0

# Função para inserir uma nova categoria-----------------------------------------
def inserir_categoria():
    exibir_subtitulo('Cadastrar categoria')
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
# Função para excluir uma categoria
    
def excluir_categoria():
    listar_categorias_sem_vinculo() 
    try:
        cd_categoria = input("Digite o código da categoria que deseja excluir: ")
        conexao = sqlite3.connect('cadastro_produtos.db')
        cursor = conexao.cursor()

        # Verificar se a categoria tem produtos vinculados
        cursor.execute("SELECT COUNT(*) FROM TB_PRODUTO WHERE CD_CATEGORIA = ?", (cd_categoria,))
        total_produtos = cursor.fetchone()[0]

        if total_produtos > 0:
            print("Esta categoria possui produtos vinculados e não pode ser excluída.")
            baleia()#listar_categorias()
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

# verifica produto
def verificar_categoria_existente_produto(cd_categoria):
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM TB_PRODUTO WHERE CD_CATEGORIA = ?", (cd_categoria,))
    resultado = cursor.fetchone()[0]
    conexao.close()
    return resultado > 0

# Função para inserir um novo produto
def inserir_produto():
    exibir_subtitulo('Cadastro de novos produtos')
    listar_categorias_cadastro()
    cd_categoria = input("Digite o código da categoria do produto: ")

    if not verificar_categoria_existente(cd_categoria):
        print("\nA categoria selecionada não está cadastrada. \n\nNão é possível cadastrar o produto.")
        
        try:
            valida = int(input('\nDeseja continuar o cadastro digite [ 1 ] ou ENTER para Voltar :  '))
            if  valida == 1 :
                inserir_produto()
                return
        except ValueError: 
                listar_produtos()
                return
    
    while True:
        descricao = input("Digite a descrição do produto: ").strip().upper()  # Remova espaços em branco e converta para maiúsculas
        if descricao:  # Verifica se a descrição não está vazia
            break
        else:
            input("Descrição não pode ser em branco. Por favor, tente novamente.")
            inserir_produto()

    try: 
        preco_input = input("Digite o preço do produto: ")
        preco_input = preco_input.replace(',', '.')  # Substitui ',' por '.'
        preco = float(preco_input)

        conexao = sqlite3.connect('cadastro_produtos.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO TB_PRODUTO (CD_CATEGORIA, DS_PRODUTO, VL_PRECO) VALUES (?, ?, ?)", (cd_categoria, descricao, preco))
        conexao.commit()
        conexao.close()
        listar_produtos()
    except ValueError:
        print('Informe o preço correto')
        return

# Função para listar categorias
def listar_categorias_cadastro():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM TB_CATEGORIA")
    categorias = cursor.fetchall()
    conexao.close()
    
    headers = ["ID", "Categoria"]
    tabela_produtos = []
    for categoria in categorias:
        tabela_produtos.append(categoria)

    print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))
    #voltar_ao_menu_principal()
    #print("\nLista de Categorias:")
    #for categoria in categorias:
    #    print(categoria)
        
# Função para listar categorias
def listar_categorias():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM TB_CATEGORIA")
    categorias = cursor.fetchall()
    conexao.close()
    
    exibir_subtitulo('Lista Categorias')
    headers = ["ID", "Categoria"]
    tabela_produtos = []
    for categoria in categorias:
        tabela_produtos.append(categoria)

    print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))
    #voltar_ao_menu_principal()
    #print("\nLista de Categorias:")
    #for categoria in categorias:
    #    print(categoria)
    menu_crud_categoria()
        
def listar_produtos():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT p.CD_PRODUTO, c.DS_CATEGORIA, p.DS_PRODUTO, p.VL_PRECO FROM TB_PRODUTO p inner join TB_CATEGORIA c on p.CD_CATEGORIA = c.CD_CATEGORIA" )
    produtos = cursor.fetchall()
    conexao.close()
    
    exibir_subtitulo('Lista de produtos')

    headers = ["ID", "Categoria", "Produto", "Preço"]
    tabela_produtos = []

    for produto in produtos:
        # Formatting the price to display two decimal places
        produto = list(produto)
        preco = "{:.2f}".format(produto[3])  # Format price to two decimal places
        if '.' not in preco:  # Check if it's a whole number
            preco += '.00'  # Add trailing zeros
        produto[3] = preco
        tabela_produtos.append(produto)
    
    print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))
    menu_crud_produto()

   
    #voltar_ao_menu_principal()
 
# Função para excluir um produto
def excluir_produto():
    cd_produto = input("Digite o código do produto que deseja excluir: ")
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM TB_PRODUTO WHERE CD_PRODUTO = ?", (cd_produto,))
    conexao.commit()
    conexao.close()
    print("Produto excluído com sucesso.")
    listar_produtos()
#exibir nome do programa
    
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
        #print("2. Editar")
        print("2. Excluir")
        #print("4. Excluir Categoria")
        #print("5. Listar Produtos")
        print('3. Voltar')
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            inserir_produto()
        #elif opcao == '2':
        #    baleia()
        #    voltar_ao_menu_principal()      
        elif opcao == '2':
            excluir_produto()

        else:
            main()

# Menu CRUD_categoria
def menu_crud_categoria():  
    while True:
        
        print("\n1. Novo")
        #print("2. Editar")
        print("2. Excluir")
        #print("4. Excluir Categoria")
        #print("5. Listar Produtos")
        print('3. Voltar')
        opcao = input("\nEscolha uma opção: ")
        if opcao == '1':
            inserir_categoria()
        #elif opcao == '2':
        #    baleia()
            voltar_ao_menu_principal()      
        elif opcao == '2':
            excluir_categoria()

        else:
            main()

# Menu principal
def menu_principal():
    while True:
        print("Menu Principal:\n")
        print("1. Produto")
        print("2. Categoria")
        #print("3. Excluir Produto")
        #print("4. Excluir Categoria")
        #print("5. Listar Produtos")
        print("3. Finalizar Sistema")
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            listar_produtos()
        elif opcao == '2':
            listar_categorias()
        elif opcao == '3':
            apaga_csv()
            exportar_para_csv()
            os.system('Cls')
            nome_grupo()
            time.sleep(2) 
            joia()
            time.sleep(2) 
            os.system('Cls')
            print('Bem vindo ao BONUS... \n')  
            opcoes = [1,2,3 ]
            opcao_escolhida = random.choice(opcoes)

            if opcao_escolhida == 1:
             
                caca_palavra ()  
                    
            elif opcao_escolhida== 2:
                jogar()
                
            os.system('Cls')
            print('''Obrigado por utilizar nosso APP...
                  
                  ''')        
            
            exit()
            
            
        else:
            voltar_ao_menu_principal()
            print("Opção inválida. Tente novamente.")


# Função principal

def main():
    global contador  # Indica que a variável contador é global
    contador += 1    # Incrementa o contador em 1
    if contador == 1 :
        abertura() 
        
    os.system('cls')
    exibir_nome_do_programa()
    criar_tabelas()
    menu_principal()

if __name__ == "__main__":
    main()
    

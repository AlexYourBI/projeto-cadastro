import sqlite3
import os
from tabulate import tabulate
from colorama import Fore, Style
from utils import baleia,abertura,exibir_subtitulo,nome_app,finalizar

contador = 0

# Função para inserir uma nova embalagem
def inserir_embalagem():
    exibir_subtitulo('Cadastrar embalagem')
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

# Função para inserir uma nova categoria
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
        cd_embalagem = input("Digite o código da embalagem que deseja excluir: ")
        conexao = sqlite3.connect('cadastro_produtos.db')
        cursor = conexao.cursor()

        # Verificar se a embalagem tem produtos vinculados
        cursor.execute("SELECT COUNT(*) FROM TB_PRODUTO WHERE CD_EMBALAGEM = ?", (cd_embalagem,))
        total_produtos = cursor.fetchone()[0]

        if total_produtos > 0:
            print("Esta embalagem possui produtos vinculados e não pode ser excluída.")
            baleia()#listar_embalagens()
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

# verifica embalagem
def verificar_embalagem_existente(cd_embalagem):
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM TB_EMBALAGEM WHERE CD_EMBALAGEM = ?", (cd_embalagem,))
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

    cd_categoria = input("Por favor, insira o [ID] correspondente à categoria do produto que você pretende cadastrar: ")
     
    if not verificar_categoria_existente(cd_categoria):
        print("\nA categoria selecionada não está cadastrada. \nNão é possível cadastrar o produto.") 
        try:
            valida = int(input('\nDeseja continuar o cadastro digite [ 1 ] ou ENTER para Voltar :  '))
            if  valida == 1 :
                inserir_produto()
                return
        except ValueError: 
                listar_produtos()
                return
    exibir_subtitulo('Cadastro de novos produtos')
    #listar_categorias_cadastro(cd_categoria)
    
    ds_categoria = obter_descricao_categoria(cd_categoria)
    
    while True:
        descricao = input(f"[ {ds_categoria} ]\nPor favor, digite a descrição do produto: ").strip().upper()  # Remova espaços em branco e converta para maiúsculas
        if descricao:  # Verifica se a descrição não está vazia
            break
        else:
            input("Descrição não pode ser em branco. Por favor, tente novamente.")
            inserir_produto()

    try: 
        exibir_subtitulo('Cadastro de novos produtos')
        preco_input = input(f"[ {ds_categoria} ] [ {descricao} ]\nInforme o preço do produto : ")
        preco_input = preco_input.replace(',', '.')  # Substitui ',' por '.'
        preco = float(preco_input)




        exibir_subtitulo('Cadastro de novos produtos')
        print (f'[ {ds_categoria} ] [ {descricao} ] [{preco}]')
        listar_embalagens_cadastro()
        
        cd_embalagem = input(f"\nDigite o [ ID ] da embalagem : ")
        
        if not verificar_embalagem_existente(cd_embalagem):
            print("\nA embalagem selecionada não está cadastrada. \n\nNão é possível cadastrar o produto.")
            try:
                valida = int(input('\nDeseja continuar o cadastro digite [ 1 ] ou ENTER para Voltar :  '))
                if  valida == 1 :
                    inserir_produto()
                    return
            except ValueError: 
                    listar_produtos()
                    return
        exibir_subtitulo('Cadastro de novos produtos')



        conexao = sqlite3.connect('cadastro_produtos.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO TB_PRODUTO (CD_EMBALAGEM,CD_CATEGORIA, DS_PRODUTO, VL_PRECO) VALUES (?, ?, ? , ?)", (cd_embalagem,cd_categoria, descricao, preco))
        conexao.commit()
        conexao.close()
        listar_produtos()
    except ValueError:
        print('Informe o preço correto')
        return

# Função para listar embalagens
def listar_embalagens_cadastro():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM TB_EMBALAGEM")
    embalagens = cursor.fetchall()
    conexao.close()
    
    headers = ["ID", "Embalagem"]
    tabela_produtos = []
    for embalagem in embalagens:
        tabela_produtos.append(embalagem)

    if len(tabela_produtos) == 0:
        print("\033[31mNão há embalagens cadastradas.\033[0m") 
        baleia()
        menu_opcao_cadastro(2)
    else:       

        print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))

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
    
    if len(tabela_produtos) == 0:
        print("\033[31mNão há categorias cadastradas.\033[0m") 
        baleia()
        menu_opcao_cadastro(1)
    else:
        print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))

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
    menu_crud_embalagem()

# Função para listar categorias
def listar_categorias():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM TB_CATEGORIA")
    categorias = cursor.fetchall()
    conexao.close()
    
    exibir_subtitulo('Cadastro de Categorias')
    headers = ["ID", "Categoria"]
    tabela_produtos = []
    for categoria in categorias:
        tabela_produtos.append(categoria)

    print(tabulate(tabela_produtos, headers=headers, tablefmt="grid"))
    menu_crud_categoria()
        
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
            #voltar_ao_menu_principal()      
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
        elif opcao == '2':
            listar_categorias()
        elif opcao == '3':
            listar_embalagens()
            main()
        elif opcao == '4':
            # Chame a função para obter o número de cadastros

            quantidade_cadastros = contar_cadastros()
            if quantidade_cadastros >=5 :
                finalizar() 
            else:
                baleia() 
                input("Para concluir, precisaremos que você cadastre pelo menos 5 produtos. Vamos lá?")
                main()
        else:
            voltar_ao_menu_principal()
            print("Opção inválida. Tente novamente.")

# Menu opcao cadastro
def menu_opcao_cadastro(parametro):
    while True:
        if parametro == 1:
            print("1. Cadastrar Categoria ")
            print("2. Voltar")
            opcao = input("\nEscolha uma opção: ")
            if opcao == '1':
                listar_categorias()
            else:
                main()
        elif parametro == 2:
            print("1. Cadastrar Embalagem ")
            print("2. Voltar")
            opcao = input("\nEscolha uma opção: ")
            if opcao == '1':
                listar_embalagens()
            else:
                main()
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
    



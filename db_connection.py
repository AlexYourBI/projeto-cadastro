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


# Função para criar as tabelas se ainda não existirem no banco de dados
def criar_tabelas():
    conexao = sqlite3.connect('cadastro_produtos.db')
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS TB_CATEGORIA (
                        CD_CATEGORIA INTEGER PRIMARY KEY,
                        DS_CATEGORIA TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS TB_PRODUTO (
                        CD_PRODUTO INTEGER PRIMARY KEY,
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
    cursor.execute('''SELECT * FROM TB_CATEGORIA''')
    categorias = cursor.fetchall()

    cursor.execute('''SELECT * FROM TB_PRODUTO''')
    produtos = cursor.fetchall()

    # Exportar dados para o arquivo CSV
    with open('categorias.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['CD_CATEGORIA', 'DS_CATEGORIA'])
        escritor_csv.writerows(categorias)

    with open('produtos.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['CD_PRODUTO', 'CD_CATEGORIA', 'DS_PRODUTO', 'VL_PRECO'])
        escritor_csv.writerows(produtos)

    conexao.close()
    # Verifica se os arquivos CSV já existem e, se sim, os exclui

def apaga_csv():
    if os.path.exists('categorias.csv'):
        os.remove('categorias.csv')

    if os.path.exists('produtos.csv'):
        os.remove('produtos.csv')
     
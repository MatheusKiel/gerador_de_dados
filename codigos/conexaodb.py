import psycopg2
import os

conexao = psycopg2.connect(host='localhost',database='postgres',user='postgres',password ='postgres')
cursor = conexao.cursor()

def consultar(sql):
    try:
        cursor.execute(sql)
        info = cursor.fetchall()
        return info
    except psycopg2.Error as error:
        print('Erro ao consultar dados: ', error)

def inserir(tabela, colunas, dados):
    try:
        cursor.execute(f"INSERT INTO {tabela} ({colunas}) VALUES ({dados})")
        conexao.commit()    # Confirma a inserção
        os.system('cls')
        print('Dado inserido')
    except psycopg2.Error as error:
        os.system('cls')
        print('Erro ao inserir dados: ', error)

def deletar(sql):
    try:
        cursor.execute(sql)
        conexao.commit()
        print('Dados removidos')
    except psycopg2.Error as error:
        print('Erro ao remover dados: ', error)

def alterar(sql):
    try:
        cursor.execute(sql)
        conexao.commit()
        print('Dados alterados!')
    except psycopg2.Error as error:
        print('Erro ao alterar dados: ', error)


def fechar_conexaodb():
    cursor.close()
    conexao.close()
    print('Conexão com banco de dados encerrada!')

    
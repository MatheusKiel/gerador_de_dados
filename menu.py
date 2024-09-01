from codigos import (conexaodb as cdb,
                     gerardados as gd)
import os


while True:
    print('Menu:')
    print('[0] - Adicionar Novo Cliente')
    print('[1] - Adicionar Novo Fornecedor')
    print('[2] - Listar Clientes')
    print('[3] - Listar Fornecedores')
    print('[4] - Sair')
    op = input('Opção: ')
    op = int(op)
    if op == 0:
        tabela, colunas, dados = gd.pessoa()
        cdb.inserir(tabela, colunas, dados)
        
    elif op == 1:
        
        tabela, colunas, dados = gd.empresa()
        cdb.inserir(tabela, colunas, dados)
    
    elif op == 2:
        os.system('cls')
        print('Função em desenvolvimento!')
        continue

    elif op == 3:
        os.system('cls')
        print('Função em desenvolvimento!')
        continue

    elif op == 4:
        os.system('cls')
        print("Você saiu do sistema!")
        break

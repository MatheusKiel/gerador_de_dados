import geradorcpf as gcpf
from faker import Faker
fakebr = Faker('pt_BR')
fakeus = Faker('en_US')

def pessoa():    
    try:
        nome = fakebr.first_name() +" "+ fakebr.last_name()
        cpf = gcpf.gerarcpf()
        email = f'{nome.lower().replace(" ","_")}@mail.com.br'
        endereco = f'{fakebr.street_name()}, {fakebr.building_number()}'
        cidade = fakebr.city()
        estado = fakebr.estado_nome()
        pais = 'Brasil'

        dados = f"'{nome}', {cpf}, '{email}', '{endereco}', '{cidade}', '{estado}', '{pais}'"
        tabela = 'clientes'
        colunas = "nome, cpf, email, endereco, cidade, estado, pais"

        return tabela, colunas, dados
    except:
        print('Erro em gerar dados de pessoa')

def empresa():
    try:
        nome_empresa = fakeus.company()
        contato = fakebr.phone_number()
        endereco = f'{fakebr.street_name()}, {fakebr.building_number()}'
        cidade = fakebr.city()
        estado = fakebr.estado_nome()
        pais = 'Brasil'

        dados = [nome_empresa, contato, endereco, cidade, estado, pais]

        dados = f"'{nome_empresa}', '{contato}', '{endereco}', '{cidade}', '{estado}', '{pais}'"
        tabela = 'fornecedores'
        colunas = "nome, contato, endereco, cidade, estado, pais"

        return tabela, colunas, dados
    except:
        print('Erro em gerar dados de empresa')


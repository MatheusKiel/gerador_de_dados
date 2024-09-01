/*CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf NUMERIC(11) NOT NULL,
    email VARCHAR(100),
    endereco TEXT,
    cidade VARCHAR(100),
    estado VARCHAR(100),
    pais VARCHAR(100)
);

CREATE TABLE fornecedores(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(50),
    endereco TEXT,
    cidade VARCHAR(100),
    estado VARCHAR(100),
    pais VARCHAR(100)
);

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    preco_custo NUMERIC(10,2),
    preco_venda NUMERIC(10,2),
    fornecedor_id INTEGER REFERENCES fornecedores(id)
);*/
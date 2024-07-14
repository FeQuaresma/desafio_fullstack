CREATE TABLE IF NOT EXISTS tipo_acao
(
    codigo_acao SERIAL PRIMARY KEY,
    nome_acao CHARACTER VARYING(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS acao
(
    id SERIAL PRIMARY KEY,
    codigo_acao INT REFERENCES tipo_acao (codigo_acao),
    investimento DOUBLE PRECISION,
    data_prevista DATE,
    data_cadastro DATE
);
# Desafio FullStack

## Começando com o Mysql

1. Baixe e instale o Docker

  - [Docker](https://www.docker.com/)

2. Dentro da pasta do projeto, entre na pasta **database** e rode o **docker run** como no exemplo abaixo.

  ```bash
    cd database
    docker run --name mysql-pharmaviews -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e MYSQL_DATABASE=db -p 3306:3306 -v $(pwd)/mysql_init:/docker-entrypoint-initdb.d -d mysql:latest
  ```

Isso vai criar um container de MySQL para o seu backend poder acessar

3. Verifique se o container está de pé com

  ```base
    docker ps
  ```

  se apareceu alguma linha abaixo do CONTAINER ID, foi um sucesso

4. **(opcional)** Caso queira interagir com o Banco de dados, pode rodar o comando

  ```bash
    docker exec -it mysql-pharmaviews mysql -u root -p
  ```

  dentro, você pode rodar comandos SQL para interagir.
  Pode dar algum erro se tentar fazer o comando logo após abrir o container, espere alguns segundos.

## Inicie o Backend

1. Execute o comando no terminal 

```bash
  python3 --version
```

Se ele forneceu uma versão ok, se não, baixe e instale o [python](https://www.python.org/downloads/)

2. Depois disso, entre na pasta backend e rode o código para gerar um ambiente python

```bash
  cd ..
  cd backend
  python3 -m venv env
  source env/bin/activate
```

desta forma, você já deve estar dentro do ambiente python

3. Instale os requirements usando o pip

```bash
  pip install -r requirements.txt
```

4. Por fim, utilize o comando com fastAPI CLI para subir o backend localmente

```bash
  fastapi run app/main.py --reload
```

5. Verifique se está funcionando acessando o link [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

6. **(opcional)** Você pode interagir com a API diretamente, vendo os paths disponíveis dentro dessa pagína.

## Iniciando o Frontend

1. Para iniciar o Frontend, basta acessar a pasta frontend e abrir o arquivo **index.html**

2. E agora pode utilizar a aplicação.

# Ferramentas

## Database

- Docker com MySQL

Usei o docker pela familiaridade que eu já tinha com a ferramenta, ela é bem simples de usar e replicar para várias situações diferentes, além de ser bem leve

## Backend

- Python

Framework:
  - Fastapi: Framework desenvolvido para facilitar a criação de um API em Python

Libs:
  - SQLAlchemy: Faz todos os envios de POST, GET, PATCH e DELETE
  - mysqlclient: Cria a conexão para enviar e receber informações do banco
  - pydantic: Faz tipagem para garantir a estrutura dos dados
  - pymysql: Facilita a conexão com o Banco de Dados
  - fastapi-cors: Liberar o acesso direto ao API sem restrição de CORS

## Frontend

  - HTML, CSS e Javascript
  - Sem Framework

Libs:
  - Bootstrap 3.4: Facilita a padroniza grande parte do CSS da pagina
  - DataTables: Cria a tabela que é mostrada os dados
  
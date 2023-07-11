# Sistema de Gerenciamento

Este é um programa em Python que está em desenvolvimento e que implementa um sistema de gerenciamento , permitindo o controle de estoque, adição, atualização e exclusão de produtos, além de autenticação de usuários.

## Funcionalidades

O sistema de gerenciamento oferece as seguintes funcionalidades:

1. Controle de estoque: Permite adicionar produtos ao estoque, atualizar informações de produtos existentes e excluir produtos do estoque.
2. Listagem de produtos: Exibe todos os produtos presentes no estoque.
3. Busca de produtos: Permite buscar produtos pelo nome, exibindo os resultados da busca.
4. Autenticação de usuários: Requer que os usuários façam login para acessar as funcionalidades do sistema.

## Requisitos

Para executar o programa, é necessário ter o Python instalado no seu computador. Além disso, são necessárias as seguintes bibliotecas Python:

- sqlite3: Para a manipulação do banco de dados SQLite.
- PyQt5: Para a criação da interface gráfica.

## Como executar

1. Clone este repositório para o seu ambiente local ou faça o download dos arquivos.
2. Certifique-se de ter as bibliotecas mencionadas acima instaladas no seu ambiente Python.
3. Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos estão localizados.
4. Execute o comando `python main.py` para iniciar o programa.

## Interface do Usuário

Ao executar o programa, você será apresentado a uma interface de login, onde deverá inserir seu nome de usuário e senha para acessar o sistema. Por padrão, o usuário pré-definido é "admin" e a senha é "1234". Você pode alterar essas credenciais no arquivo `DB.db`.

Após fazer o login, você terá acesso às funcionalidades do sistema, que incluem adicionar produtos, listar produtos, buscar produtos, atualizar produtos e excluir produtos. Você pode interagir com o sistema usando a interface gráfica fornecida.

## Banco de Dados

O programa utiliza um banco de dados SQLite para armazenar os dados do estoque. O arquivo `DB.db` é criado automaticamente ao executar o programa pela primeira vez e contém a tabela "usuarios" com os campos "id" (chave primária), "usuario", "nome", "cargo" e "senha".

## Etapa do Projeto

Interface e sistema de Login ✔

Interface e sistema de Register ✔

Tela principal ✔

Fluxo de produtos 

Geração de planilhas

Importação de XML

## Atualizações

1.0: Listagem de produtos funcional, login e cadastro funcionando, cadastro de produtos em produção




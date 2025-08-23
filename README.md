# <p align='center'> Cadastramento de usuários via / no MongoDB

Projeto de gerenciamento de dados cadastrados pelo usuário, com fase inicial de desenvolvimento

- Projeto escalável
- Open-source

<br>

## 🖥️Tecnologias utilizadas:

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,mongodb,pymongo" />
  </a>
</p>

## Estrutura de Pastas:

```
projeto
  |- src/
  |   |- database/
  |      |- mongodb.py 
  |   |- utils/
  |      
  |   |- main.py
  |
  |- .gitignore
  |- .env
  |- README.md
```

- `database`- pasta que vai conter funcionalidades relacionadas ao database
- `utils`- pasta que vai conter funcionalidades gerais
- `main.py`- Arquivo que vai conter o código principal

<br>

## Como usar:

- clone o repositório usando: `git clone https://github.com/lowwryzen/Cadastramento-de-usuarios.git`

<br>

- crie um arquivo `.env` com as seguintes informações:
`DB_URI = "<seu_database_URI>"`
`DB_NAME = "<seu_database_NAME>"`
# Django API CRUD

Uma API REST simples criada com Django e Django REST Framework para gerenciamento de usuários. Este projeto fornece uma base sólida para criar, ler, atualizar e excluir perfis de usuário.

## Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes do Python)
- virtualenv (opcional, mas recomendado)

## Instalação

1. **Clone o repositório:**

   ```bash
   https://github.com/Gustavo-PGM/API_Rest.git

2. **Crie um ambiente virtual e ative-o (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt

4. **Configure o banco de dados:**

   Execute as migrações para configurar o banco de dados:

    ```bash
     python manage.py makemigrations
     python manage.py migrate


5. **Inicie o servidor de desenvolvimento:**

   ```bash
    python manage.py runserver

A API estará disponível em http://127.0.0.1:8000/.


8. **Funcionalidades da API:**
  Esta API utiliza Django REST Framework para fornecer os seguintes endpoints para gerenciamento de usuários:

        GET - Listar todos os usuários
        POST - Criar um novo usuário
        PUT - Atualizar um usuário existente
        DELETE - Excluir um usuário

7. **Estrutura de Pastas:**
   ```bash
    core/: Código do sistema, incluindo configurações e URLs.
    app/: Código do sistema, incluindo modelos, visualizações e URLs.
    static/: Arquivos estáticos como CSS, JavaScript e imagens.
    media/: Arquivos carregados pelo usuário, como imagens de postagens.
    templates/: Templates HTML usados para renderizar as páginas.
    requirements.txt: Lista de dependências do projeto.
    manage.py: Script de gerenciamento do Django.


Contato
Se tiver dúvidas ou precisar de ajuda, abra uma issue no GitHub ou entre em contato com gustavo.cavalcante.gomes06@gmail.com.

Este README.md inclui detalhes sobre a instalação, configuração e uso da API, destacando o uso do Django REST Framework. Sinta-se à vontade para ajustar conforme necessário.

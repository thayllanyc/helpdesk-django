# Sistema de Chamados (Helpdesk)

Sistema de gerenciamento de chamados de suporte, desenvolvido em Django, com controle de acesso baseado em papéis (Cliente, Agente e Administrador).

Projeto desenvolvido como parte do meu aprendizado prático em desenvolvimento web com Python/Django.

## Funcionalidades

- Autenticação de usuários com tela de login própria
- Três papéis de usuário com permissões diferentes:
  - **Cliente**: abre chamados e acompanha o andamento dos próprios chamados
  - **Agente**: visualiza e gerencia os chamados atribuídos a ele
  - **Administrador**: tem acesso total a todos os chamados do sistema
- Abertura de chamados via formulário
- Gerenciamento de status (Aberto, Em andamento, Resolvido, Fechado)
- Atribuição de agente responsável
- Sistema de comentários por chamado
- Filtros por status e busca por título
- Paginação da listagem de chamados
- Dashboard com contagem de chamados por status
- Testes automatizados cobrindo as regras de permissão

## Tecnologias utilizadas

- Python
- Django
- SQLite (banco de dados de desenvolvimento)
- HTML + Django Template Language

## Como rodar o projeto localmente

1. Clone o repositório:
```bash
git clone https://github.com/thayllanyc/helpdesk-django.git
cd helpdesk-django
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Instale as dependências:
```bash
pip install django
```

4. Rode as migrations:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Rode o servidor:
```bash
python manage.py runserver
```

7. Acesse `http://127.0.0.1:8000/chamados/login/`

## Rodando os testes

```bash
python manage.py test chamados
```

## Estrutura do projeto

- `core/` — configurações do projeto Django
- `contas/` — app responsável pela autenticação e modelo de usuário customizado
- `chamados/` — app principal, com os modelos de Categoria, Chamado e Comentário, e toda a lógica de permissões

## Autora

Thayllany Correa
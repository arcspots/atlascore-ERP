# AtlasCore ERP

Backend ERP multi-tenant desenvolvido com FastAPI seguindo princípios de Clean Architecture.

## Tecnologias

* Python 3.11
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* JWT Authentication
* Pytest

---

## Funcionalidades

* Multi-tenant
* Autenticação JWT
* Controle de permissões por Role
* Criação de empresas
* Criação de usuários
* Hash seguro de senhas
* Validação de acesso entre empresas
* Testes automatizados

---

## Estrutura do Projeto

```bash
app/
├── application/
├── domain/
├── infrastructure/
├── interfaces/
```

---

## Instalação

```bash
git clone <repo>
cd atlascore-erp

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Configuração

Criar arquivo `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/atlascore
JWT_SECRET_KEY=your_secret
```

---

## Executar API

```bash
uvicorn main:app --reload
```

---

## Executar testes

```bash
pytest -v
```

---

## Documentação Swagger

Acesse:

```txt
http://127.0.0.1:8000/docs
```

---

## Arquitetura

O projeto utiliza:

* Clean Architecture
* Separação entre domínio, aplicação e infraestrutura
* Repositories Pattern
* Use Cases
* Dependency Injection

---

## Segurança

* JWT Authentication
* Password Hashing
* Isolamento multi-tenant
* Controle de permissões ADMIN / USER

---

## Status

Projeto em desenvolvimento.

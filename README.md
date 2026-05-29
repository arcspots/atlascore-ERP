# AtlasCore ERP

Backend ERP multi-tenant desenvolvido com FastAPI utilizando princípios de Clean Architecture, isolamento entre empresas (tenant isolation), autenticação JWT e arquitetura escalável para sistemas SaaS corporativos.

---

# Visão Geral

O AtlasCore ERP é um backend estruturado para suportar aplicações empresariais modernas com:

* autenticação segura
* separação de domínio
* controle de permissões
* multi-tenancy
* arquitetura desacoplada
* escalabilidade modular

O projeto foi desenhado pensando em evolução futura para:

* plataformas SaaS
* sistemas financeiros
* painéis administrativos
* observabilidade
* auditoria
* módulos de segurança
* integrações corporativas
* EDR/Security SaaS

---

# Tecnologias

* Python 3.11
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* JWT Authentication
* Pytest
* Passlib / BCrypt

---

# Funcionalidades Implementadas

## Multi-Tenant

Cada empresa possui isolamento lógico completo.

Usuários autenticados não conseguem acessar ou criar recursos pertencentes a outra empresa.

---

## Autenticação JWT

Sistema completo de autenticação utilizando tokens JWT contendo:

* user_id
* role
* company_id
* expiração

---

## RBAC (Role-Based Access Control)

Controle de permissões baseado em roles:

* ADMIN
* USER

Somente administradores podem criar novos usuários.

---

## Segurança

* Hash seguro de senhas com BCrypt
* Validação de permissões
* Isolamento entre tenants
* Proteção contra acesso cross-company
* Autenticação Bearer Token

---

## Estrutura em Clean Architecture

Separação clara entre:

* domínio
* aplicação
* infraestrutura
* interfaces HTTP

O domínio permanece desacoplado do framework.

---

## Repository Pattern

Implementação desacoplada de acesso a dados:

* InMemory repositories
* PostgreSQL repositories

Facilitando:

* testes
* manutenção
* troca de banco
* escalabilidade

---

## Migrations

Versionamento do banco utilizando Alembic.

---

## Testes Automatizados

Cobertura inicial utilizando Pytest:

* criação de empresa
* duplicidade de documento
* permissões ADMIN
* bloqueio de acesso indevido
* isolamento multi-tenant

---

# Estrutura do Projeto

```bash
app/
└── core/
    ├── application/
    │   ├── dto/
    │   └── use_cases/
    │
    ├── domain/
    │   ├── entities/
    │   ├── enums/
    │   ├── exceptions/
    │   └── services/
    │
    ├── infrastructure/
    │   ├── config/
    │   ├── database/
    │   │   ├── models/
    │   │   └── repositories/
    │   │
    │   └── security/
    │
    ├── interfaces/
    │   └── http/
    │       ├── routes/
    │       └── schemas/
    │
    └── scripts/
```

---

# Fluxo Atual do Sistema

## Empresas

* criação de empresa
* validação de documento único

## Usuários

* criação de usuários
* autenticação JWT
* validação de role
* vínculo obrigatório com empresa

## Autorização

* ADMIN pode criar usuários
* USER não pode criar usuários
* usuários não podem operar em outra empresa

---

# Instalação

```bash
git clone https://github.com/arcspots/atlascore-ERP.git

cd atlascore-ERP

python -m venv venv
```

---

# Ativar ambiente virtual

## Windows

```bash
venv\Scripts\activate
```

## Linux/macOS

```bash
source venv/bin/activate
```

---

# Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Configuração

Criar arquivo `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/atlascore

JWT_SECRET_KEY=your_secret_key
```

---

# Executar migrations

```bash
alembic upgrade head
```

---

# Executar API

```bash
uvicorn main:app --reload
```

---

# Swagger

Documentação automática disponível em:

```txt
http://127.0.0.1:8000/docs
```

---

# Seed Inicial de Administrador

```bash
python -m app.core.scripts.seed_admin
```

---

# Executar Testes

```bash
pytest -v
```

---

# Arquitetura

O projeto utiliza:

* Clean Architecture
* Repository Pattern
* Use Cases
* Dependency Injection
* DTO separation
* Domain isolation
* Layered architecture

---

# Roadmap

## Próximos módulos

* auditoria de eventos
* logs centralizados
* observabilidade
* métricas
* filas assíncronas
* event-driven architecture
* painel administrativo
* módulos financeiros
* integração com mensageria
* cache distribuído
* monitoramento
* sistema de permissões granular
* EDR/Security modules

---

# Objetivo do Projeto

O AtlasCore ERP foi criado como estudo avançado de arquitetura backend moderna, sistemas SaaS multi-tenant e engenharia de software aplicada a ambientes corporativos.

---

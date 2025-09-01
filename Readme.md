# Contabilipy

Contabilipy é uma aplicação Python para gestão contábil e gerenciamento de arquivos, com backend em FastAPI e interface em Streamlit.
O projeto é containerizado com Docker e possui ambientes separados para **desenvolvimento** e **produção**.

---

## 🗂 Estrutura do projeto

```
📂 contabilipy
 ├── backend/          # Backend Python (FastAPI)
 ├── interface/        # Interface Streamlit
 ├── docker-compose.yaml          # Compose produção
 ├── docker-compose-dev.yaml      # Compose dev com hot reload
 ├── cz.yaml                     # Config Commitizen
 ├── .gitignore
 └── .dockerignore
```

---

## ⚡ Pré-requisitos

* Docker >= 20.10
* Docker Compose >= 1.29
* Python 3.11 (somente para dev local, se necessário)

---

## 🏃 Rodando o projeto

### Desenvolvimento

Hot reload para backend e interface:

```bash
docker-compose -f docker-compose-dev.yaml up
```

Ou em background:

```bash
docker-compose -f docker-compose-dev.yaml up -d
```

Parar o ambiente:

```bash
docker-compose -f docker-compose-dev.yaml down
```

Rebuildar containers após mudanças no Dockerfile:

```bash
docker-compose -f docker-compose-dev.yaml up --build
```

Logs de um serviço específico:

```bash
docker-compose -f docker-compose-dev.yaml logs -f backend
```

---

### Produção

```bash
docker-compose up -d
```

Os serviços serão expostos nas portas:

* Backend: `8000`
* Interface: `8501`
* MySQL: `3306`

---

## 🛠 Tecnologias

* Python 3.11
* FastAPI (Backend)
* Streamlit (Interface)
* MySQL (Banco de dados)
* Docker / Docker Compose

---

## 📝 Convenção de commits

Usamos **Conventional Commits** com Commitizen (`cz.yaml`):

* `feat`: nova funcionalidade
* `fix`: correção de bug
* `chore`: mudanças de infraestrutura, Docker, env, gitignore

Exemplo:

```bash
git commit -m "chore: atualizar docker-compose e gitignore"
```


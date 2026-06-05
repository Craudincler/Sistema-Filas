# Sistema de Filas com FastAPI, Celery e Redis

Projeto backend desenvolvido em Python para demonstrar o uso de filas assíncronas utilizando FastAPI, Celery e Redis.

---

## Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- Celery
- Redis
- SQLite
- SQLAlchemy
- Docker
- VS Code

---

## Arquitetura

```text
Usuário
   ↓
FastAPI
   ↓
SQLite
   ↓
Redis (Fila)
   ↓
Celery Worker
   ↓
Atualização de Status
```

---

## Fluxo do Sistema

1. O usuário envia uma solicitação para criar uma tarefa.
2. A API salva a tarefa no banco de dados.
3. A API envia a tarefa para a fila Redis.
4. O Worker Celery consome a tarefa.
5. O status muda para "processing".
6. Após finalizar o processamento, o status muda para "completed".
7. O usuário pode consultar o status da tarefa.

---

# Instalação e Execução

## Pré-requisitos

Antes de iniciar, instale:

### Python

Verifique:

```bash
python --version
```

### Docker

Verifique:

```bash
docker --version
```

### Git

Verifique:

```bash
git --version
```

---

## 1. Clonar o repositório

```bash
git clone https://github.com/Craudincler/Sistema-Filas.git
```

Entrar na pasta:

```bash
cd sistema-filas-fastapi-celery
```

---

## 2. Criar ambiente virtual

Windows:

```bash
python -m venv .venv
```

---

## 3. Ativar ambiente virtual

PowerShell:

```bash
.\.venv\Scripts\Activate
```

CMD:

```cmd
.venv\Scripts\activate.bat
```

Linux/Mac:

```bash
source .venv/bin/activate
```

Após ativar deverá aparecer:

```text
(.venv)
```

no início do terminal.

---

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

Verificar instalação:

```bash
pip list
```

---

## 5. Iniciar Redis

### Verificar se o container existe

```bash
docker ps -a
```

### Caso já exista

```bash
docker start redis-fila
```

### Caso não exista

```bash
docker run -d --name redis-fila -p 6379:6379 redis:latest
```

Verificar se está ativo:

```bash
docker ps
```

Resultado esperado:

```text
redis-fila
Up
6379->6379
```

---

## 6. Iniciar API FastAPI

Abra um terminal:

```bash
uvicorn app.main:app --reload
```

Resultado esperado:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

## 7. Abrir documentação Swagger

No navegador:

```text
http://127.0.0.1:8000/docs
```

A documentação interativa da API deverá aparecer.

---

## 8. Iniciar Worker Celery

Abra um segundo terminal.

Ative novamente o ambiente virtual:

```bash
.\.venv\Scripts\Activate
```

Execute:

```bash
celery -A app.tasks worker --loglevel=info --pool=solo
```

Resultado esperado:

```text
ready
```

---

## Testando o Sistema

### Criar uma tarefa

Endpoint:

```http
POST /jobs
```

Body:

```json
{
  "task_name": "Gerar relatório mensal"
}
```

Resposta:

```json
{
  "id": 1,
  "task_name": "Gerar relatório mensal",
  "status": "pending",
  "result": null
}
```

---

### Consultar tarefa

Endpoint:

```http
GET /jobs/1
```

Status possíveis:

```text
pending
processing
completed
failed
```

Exemplo:

```json
{
  "id": 1,
  "task_name": "Gerar relatório mensal",
  "status": "completed",
  "result": "Tarefa processada com sucesso."
}
```

---

## Estrutura do Projeto

```text
fila_backend/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── celery_app.py
│   └── tasks.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── jobs.db
```

---

## Evidências de Funcionamento

Para validar o projeto:

1. Print do Docker com Redis ativo.
2. Print da API rodando.
3. Print do Swagger.
4. Print do Worker Celery.
5. Print da criação da tarefa.
6. Print do status completed.
7. Print dos logs do Worker.

---

## Autor

Lucas Claudino

Projeto desenvolvido para fins acadêmicos e demonstração de conhecimentos em Backend Python, Processamento Assíncrono e Sistemas de Filas.
# Sistema de Filas com FastAPI, Celery e Redis

Projeto backend desenvolvido em Python para demonstrar o uso de filas assíncronas com FastAPI, Celery e Redis.

## Tecnologias utilizadas

- Python
- FastAPI
- Celery
- Redis
- SQLite
- SQLAlchemy
- Docker

## Objetivo

O objetivo do projeto é simular o processamento de tarefas em segundo plano. A API recebe uma solicitação, registra a tarefa no banco de dados, envia para a fila Redis e o worker Celery processa essa tarefa de forma assíncrona.

## Fluxo do sistema

1. O usuário cria uma tarefa pela API.
2. A tarefa é salva no banco com status `pending`.
3. A tarefa é enviada para a fila Redis.
4. O worker Celery consome a tarefa.
5. O status muda para `processing`.
6. Após o processamento, o status muda para `completed`.

## Como executar o projeto

1. Clonar o repositório.
2. Instalar as dependências com `pip install -r requirements.txt`.    
3. Rodar o servidor com `uvicorn main:app --reload`.    
4. Acessar a API em http://localhost:8000. 



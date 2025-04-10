# 🔢 Desafio FPF Tech - Processamento Assíncrono com Django, Celery, RabbitMQ e Angular

Este projeto é uma aplicação web que permite o envio de três números, processando-os de forma assíncrona com **Celery** e **RabbitMQ**. O backend calcula a **média** e a **mediana**, e os resultados deveriam ser exibidos via frontend em **Angular**.

> ⚠️ **Observação importante**: Atualmente, o frontend **não está conseguindo se conectar ao backend**. A integração ainda está sendo ajustada.  
> Por outro lado, as partes do **backend, worker Celery, RabbitMQ e Docker** estão funcionando perfeitamente.

---

## 🧱 Arquitetura

- **Frontend**: Angular (Standalone)
- **Backend**: Django + Django REST Framework
- **Assíncrono**: Celery + RabbitMQ
- **Contêineres**: Docker + Docker Compose

---

## 📦 Estrutura do Projeto

```bash
.
├── api/
├── desafio_fpf/        # Projeto Django
│   ├── settings.py
│   └── ...
├── frontend/           # Projeto Angular
│   ├── src/
│   └── Dockerfile
├── manage.py
├── docker-compose.yml
└── README.md
```

---

## 🚀 Como Rodar o Projeto

### 1. Pré-requisitos

- Docker
- Docker Compose

### 2. Clonar o repositório

```bash
git clone https://github.com/andre-jnr/desafio-fpf.git
cd sua-pasta
```

### 3. Subir os serviços

```bash
docker compose up --build
```

Os seguintes serviços serão iniciados:

- 🐇 RabbitMQ em `localhost:15672` (user: `user`, senha: `password`)
- 🔙 Backend em `localhost:8000`
- 🔁 Celery worker
- 💻 Frontend Angular em `localhost:4200` (sem conexão com o backend no momento)

---

## 🌐 Acesso às Interfaces

| Serviço    | URL                             |
|------------|----------------------------------|
| Frontend   | http://localhost:4200/          |
| Backend    | http://localhost:8000/api/      |
| RabbitMQ   | http://localhost:15672/         |

---

## 🧠 Funcionalidade Esperada

1. O usuário insere 3 números no frontend.
2. Os dados são enviados ao backend (Django).
3. Uma task Celery é disparada para calcular a média e a mediana.
4. A task roda de forma assíncrona com RabbitMQ.
5. O frontend consulta o status da tarefa e exibe o resultado.

> ⚠️ A funcionalidade do frontend está incompleta devido à falha na comunicação com o backend.

---

## 🛠️ Tecnologias Utilizadas

- **Django** / **Django REST Framework**
- **Celery**
- **RabbitMQ**
- **Angular (Standalone)**
- **Docker / Docker Compose**

---

## 📁 Variáveis de Ambiente

As variáveis estão configuradas no `docker-compose.yml`:

```yaml
environment:
  RABBITMQ_DEFAULT_USER: user
  RABBITMQ_DEFAULT_PASS: password
  CELERY_BROKER_URL: amqp://user:password@rabbitmq:5672//
```

---

## 📌 Notas de Desenvolvimento

- O frontend tenta se comunicar com o backend usando o host `backend` (nome do serviço Docker).
- Verifique a URL da API no Angular:

```ts
// frontend/src/environments/environment.ts
export const environment = {
  production: false,
  apiUrl: 'http://backend:8000/api'
};
```

- Caso o problema de conexão persista, recomenda-se testar a API via ferramentas como Insomnia para garantir que o backend esteja respondendo corretamente.

---

## ✍️ Autor

Desenvolvido por [André Júnior](https://www.linkedin.com/in/andre-jnr/).  
Este projeto foi criado como parte de um desafio técnico para a FPF Tech.

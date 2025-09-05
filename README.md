# Agentic AI Portal (LangChain, Ollama, Django, MongoDB, React)

## Quickstart

1. **Clone the repo:**
    ```bash
    git clone https://github.com/rajjaware/ai_demo.git
    cd ai_demo
    ```

2. **Build and run all services:**
    ```bash
    docker-compose up --build
    ```

3. **After Ollama is running, pull a model:**
    ```bash
    docker exec -it ai_demo-ollama-1 ollama pull llama3
    ```

4. **Migrate Django DB:**
    ```bash
    docker exec -it ai_demo-backend-1 python manage.py migrate
    ```

5. **Create superuser (optional):**
    ```bash
    docker exec -it ai_demo-backend-1 python manage.py createsuperuser
    ```

6. **Access the frontend:**  
    [http://localhost:3000](http://localhost:3000)

7. **Try the agentic chat!**

---

## Structure

- `backend/`   — Django + Djongo (MongoDB)
- `frontend/`  — React
- `agent/`     — LangChain Agent (FastAPI)
- `docker-compose.yml`
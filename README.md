# Project Setup Guide

## Prerequisites
Ensure the following dependencies are installed on your Windows system:

1. **Python (3.8 or later)**
   - Download: https://www.python.org/downloads/windows/
   - Verify installation:
     ```powershell
     python --version
     pip --version
     ```

2. **Docker Desktop**
   - Download: https://www.docker.com/products/docker-desktop
   - Ensure it is installed and running.
   - Verify installation:
     ```powershell
     docker --version
     ```

3. **Git**
   - Download: https://git-scm.com/downloads
   - Verify installation:
     ```powershell
     git --version
     ```

4. **Node.js (16 or later) & npm**
   - Download: https://nodejs.org/
   - Verify installation:
     ```powershell
     node --version
     npm --version
     ```

---

## Setup Instructions

### 1. Clone the Repository
```powershell
git clone <repository-url>
cd <project-folder>
```

---

### 2. Set Up Python Environment

1. Navigate to the backend folder:
    ```powershell
    cd backend
    ```

2. Create and activate a virtual environment:
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. Install dependencies:
    ```powershell
    pip install -r requirements.txt
    ```

---

### 3. Start Docker Automatically (Optional)
To start Docker without manual intervention, follow these steps:

1. Create a file named `start_docker.sh` with the following content:
    ```bash
    #!/bin/bash
    echo "Starting Docker Desktop..."
    "C:/Program Files/Docker/Docker/Docker Desktop.exe" &
    sleep 10
    docker ps > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        echo "Docker is running successfully."
    else
        echo "Docker failed to start. Please check Docker Desktop."
    fi
    ```

2. Run the script using Git Bash:
    ```bash
    chmod +x start_docker.sh
    ./start_docker.sh
    ```

---

### 4. Run the Backend Server

Navigate to the backend folder and start the FastAPI server with:

```powershell
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will be available at `http://localhost:8000`.

---

### 5. Run the Frontend (React + Vite)

Navigate to the frontend folder and start the development server:

```powershell
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173`.

---

### 6. Test the API

Once the server is running, access the interactive API documentation at:

[http://localhost:8000/docs](http://localhost:8000/docs)

You can also test using `curl`:

```powershell
curl -X POST "http://localhost:8000/execute_code" `
     -H "Content-Type: application/json" `
     -d "{\"code\": \"print('Hello, World!')\", \"language\": \"python\"}"
```

---

### 7. Stopping the Backend and Frontend Servers
To stop the backend server, press `CTRL + C` in the terminal where it's running.

To stop the frontend server, press `CTRL + C` in the terminal where it's running.

---

## Troubleshooting

- **Docker not found error:** Ensure Docker Desktop is running.
  ```powershell
  start-process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
  ```

- **Port already in use error:** Change the port in the command when running the backend.
  ```powershell
  uvicorn main:app --host 0.0.0.0 --port 8001 --reload
  ```

---

Enjoy coding!


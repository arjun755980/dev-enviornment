import os
import subprocess
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  # Frontend URL, adjust if needed
]

# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow requests from these origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

class CodeRequest(BaseModel):
    code: str
    language: str

@app.post("/execute_code")
async def execute_code(data: CodeRequest):
    code = data.code
    language = data.language

    # Directory for saving code files
    os.makedirs("C:/Users/jesvi/project/tmp", exist_ok=True)
    file_name = os.path.join("C:/Users/jesvi/project/tmp", "main.py")  # Save directly to your desired location
    if language == "python":
        file_name = "C:/Users/jesvi/project/tmp/main.py"  # Python file name
    elif language == "javascript":
        file_name = "C:/Users/jesvi/project/tmp/main.js"  # Change for JS file
    else:
        raise HTTPException(status_code=400, detail="Unsupported language")

    try:
        # Write the code to the file
        with open(file_name, "w") as file:
            file.write(code)

        # Check if the file is written correctly
        if not os.path.exists(file_name):
            raise Exception(f"File {file_name} was not created!")

        with open(file_name, "r") as file:
            content = file.read()
            if not content.strip():
                raise Exception(f"File {file_name} is empty!")

        print(f"File {file_name} successfully created with content:\n{content}")

        # Spin up the Docker container to execute the code
        result = run_code_in_docker(file_name, language)

        return {"message": "Code executed", "output": result}
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": str(e)}

def run_code_in_docker(file_name: str, language: str) -> str:
    try:
        if language == "python":
            docker_image = "python:3.9-slim"
            command = "python /app/main.py"
        elif language == "javascript":
            docker_image = "node:14-slim"
            command = "node /app/main.js"
        else:
            raise ValueError("Unsupported language")

        # Convert the path to Unix-compatible format for Docker
        docker_mount_path = file_name.replace("\\", "/")
        docker_mount_path = docker_mount_path.replace("C:", "/mnt/c") if os.name == "nt" else docker_mount_path

        # Updated Docker run command with explicit file path
        docker_run_command = [
            "docker", "run", "--rm",
            "--memory", "256m", "--cpus", "0.5",
            "-v", f"{docker_mount_path}:/app/main.py:ro",
            docker_image,
            "sh", "-c", command
        ]

        print("Running Docker Command:", " ".join(docker_run_command))

        # Execute the Docker command
        result = subprocess.run(docker_run_command, capture_output=True, text=True)
        print("Docker stdout:", result.stdout)
        print("Docker stderr:", result.stderr)

        if result.returncode != 0:
            raise Exception(result.stderr.strip())

        return result.stdout.strip()
    except Exception as e:
        print("Error running Docker:", str(e))
        return str(e)

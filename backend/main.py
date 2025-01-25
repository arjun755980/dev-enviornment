from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os
import uuid
import docker
from fastapi.middleware.cors import CORSMiddleware

client = docker.from_env()
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

# Pydantic model to validate the incoming JSON data
class CodeRequest(BaseModel):
    code: str
    language: str

@app.post("/execute_code")
async def execute_code(data: CodeRequest):
    code = data.code
    language = data.language

    extensions = {"python": "py", "javascript": "js", "c": "c", "typescript": "ts", "java": "java"}
    if language not in extensions:
        raise HTTPException(status_code=400, detail="Unsupported language")

    file_extension = extensions[language]
    unique_id = str(uuid.uuid4())
    
    file_name = f"backend/temp/{unique_id}.{file_extension}"
    
    try:
        abs_file_path = os.path.abspath(file_name)

        file_directory = os.path.dirname(abs_file_path)
        if not os.path.exists(file_directory):
            os.makedirs(file_directory)

        with open(abs_file_path, "w") as file:
            file.write(code)

        # Spin up the Docker container to execute the code
        result = run_code_in_docker(abs_file_path, language)

        #os.remove(file_name)

        return {"message": "Code executed", "output": result}
    except Exception as e:
        return {"error": str(e)}

# Function to run the code inside a Docker container
def run_code_in_docker(file_name: str, language: str) -> str:
    try:
        if language == "python":
            docker_image = "python:3.8-slim"
            command = f"python /app/{os.path.basename(file_name)}"
        elif language == "javascript":
            docker_image = "node:14-slim"
            command = f"node /app/{os.path.basename(file_name)}"
        elif language == "c":
            docker_image = "gcc:latest"

            command = f"gcc /app/{os.path.basename(file_name)} -o /app/output && /app/output"
        elif language == "typescript":
            docker_image = "node:14-slim"
 
            command = f"npm install -g typescript && tsc /app/{os.path.basename(file_name)} && node /app/{os.path.basename(file_name).replace('.ts', '.js')}"
        elif language == "java":
            docker_image = "openjdk:11-jdk"

            command = f"javac /app/{os.path.basename(file_name)} && java /app/{os.path.basename(file_name).replace('.java', '')}"
        else:
            raise ValueError("Unsupported language")

        docker_run_command = [
            "docker", "run", "--rm", 
            "-v", f"{file_name}:/app/{os.path.basename(file_name)}",
            docker_image, 
            "sh", "-c", command
        ]

        result = subprocess.run(docker_run_command, capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return str(e)

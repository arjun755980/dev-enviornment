from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import WebSocket
from websocket import stream_logs
import subprocess
import os
import uuid

#from docker_manager import create_container 

app = FastAPI()



# Pydantic model to validate the incoming JSON data
class CodeRequest(BaseModel):
    code: str
    language: str

@app.post("/execute_code/")
async def execute_code(data: CodeRequest):
    code = data.code
    language = data.language
    # print(code)
    # Save the code to a file (based on the language)
    
    # file_name = "/tmp/code_to_run"
    # if language == "python":
    #     file_name += ".py"
    # elif language == "javascript":
    #     file_name += ".js"
    # else:
    #     raise HTTPException(status_code=400, detail="Unsupported language")

    extensions = {"python": "py", "javascript": "js"}
    if language not in extensions:
        raise HTTPException(status_code=400, detail="Unsupported language")

    # Create a unique filename
    file_extension = extensions[language]
    unique_id = str(uuid.uuid4())
    file_name = f"/home/acer/temp/{unique_id}.{file_extension}"

    try:
        with open(file_name, "w") as file:
            file.write(code)

        # Spin up the Docker container to execute the code
        result = run_code_in_docker(file_name, language)

        #os.remove(file_name)

        return {"message": "Code executed", "output": result}
    except Exception as e:
        return {"error": str(e)}

# Function to run the code inside a Docker container
def run_code_in_docker(file_name: str, language: str) -> str:
    try:
        # Define the docker image and command based on the language
        if language == "python":
            docker_image = "python:3.8-slim"
           # command = f"python {file_name}"
            command = f"python /app/{os.path.basename(file_name)}"
        elif language == "javascript":
            docker_image = "node:14-slim"
            #command = f"node {file_name}"
            command = f"node /app/{os.path.basename(file_name)}"
        else:
            raise ValueError("Unsupported language")

        # Running the container with the code
        # docker_run_command = [
        #     "docker", "run", "--rm", 
        #     "-v", f"{file_name}:/code/{file_name}", 
        #     docker_image, 
        #     "sh", "-c", command
        # ]

        docker_run_command = [
             "docker", "run", "--rm", 
             #"-v", f"{os.path.abspath(file_name)}:/code/{os.path.basename(file_name)}", 
             "-v", f"{file_name}:/app/{os.path.basename(file_name)}",
             docker_image, 
             "sh", "-c", command
        ]

        # docker_run_command = [
        #     "docker", "run", "--rm", 
        #     "-v", f"{os.path.abspath(file_path)}:/code/{os.path.basename(file_path)}", 
        #     docker_image, 
        #     "sh", "-c", command
        # ]

        # Execute the command and capture the output
        result = subprocess.run(docker_run_command, capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return str(e)

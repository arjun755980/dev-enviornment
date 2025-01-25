# Online Judge with Dynamic Isolation

## Overview
This project implements an online coding judge system that allows users to submit code, which is executed inside a dynamically spun-up Docker container. Each submission is isolated to ensure security by restricting access to host resources. The system is built using FastAPI for the backend and Docker for containerization. It supports multiple programming languages and returns the execution output to the user.

## Features
- **Dynamic Code Execution:** Each code submission runs inside its own Docker container.
- **Security Isolation:** Docker ensures that the code execution is isolated from the host system to prevent security vulnerabilities.
- **Language Support:** Currently supports Python, C, C++, JavaScript, and TypeScript for code submissions.
- **API Integration:** Submissions are handled through the `/execute_code/` endpoint which accepts the code and language.
- **Resource Efficiency:** Docker containers are created and removed dynamically to ensure efficient resource allocation.

## Tools and Technologies
- **Backend:** FastAPI (Python)
- **Containerization:** Docker
- **Programming Languages Supported:** Python, C, C++, JavaScript, TypeScript
- **Security:** Docker containers for sandboxed execution
- **Deployment:** Local server setup using Docker

## How it Works
1. **Code Submission:** Users submit their code via a POST request to the `/execute_code/` endpoint, specifying the programming language and code.
2. **Dynamic Container Creation:** Based on the programming language, a Docker container is spun up to execute the submitted code.
3. **Execution:** 
   - The code is written to a file inside the container.
   - The appropriate compiler or interpreter runs the code:
     - **Python:** Executed using `python3`.
     - **C and C++:** Compiled using `gcc` or `g++` and then executed.
     - **JavaScript:** Executed using `node`.
     - **TypeScript:** Transpiled to JavaScript using `tsc` and then executed using `node`.
4. **Output Return:** The container executes the code and returns the output or error messages to the user.
5. **Security:** The system ensures that each container is isolated from the host system, preventing unauthorized access to host resources.

## Testing the API
You can test the code execution endpoint with a POST request. For example, using `curl`:

### Python Example
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/execute_code/' \
  -H 'Content-Type: application/json' \
  -d '{
  "code": "print(\"Hello, World!\")",
  "language": "python"
}'

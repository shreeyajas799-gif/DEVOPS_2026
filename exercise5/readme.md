# Exercise 5: Docker Security with AppArmor and Python

## Objective
Secure a Python Flask application running in Docker using AppArmor security profiles and the Docker SDK for Python.

## Technologies
- Python
- Flask
- Docker
- AppArmor
- Docker SDK for Python

## Features
- Containerizes a Flask web application.
- Applies AppArmor profiles to restrict file access and binary execution.
- Uses the Docker SDK to run and inspect containers.
- Tests restricted actions such as reading sensitive files and executing binaries.

## Run the Application

Build the Docker image:

```bash
docker build -t flask-apparmor .
```

Run the container:

```bash
docker run -d --name flask-security-test -p 5001:5000 flask-apparmor
```

Access the application at http://localhost:5001.

## AppArmor Setup
AppArmor profile enforcement requires a compatible Linux environment with AppArmor enabled. Docker Desktop on macOS does not directly support loading host AppArmor profiles.

## Expected Outcome
A containerized Flask application with Docker SDK integration and tests for AppArmor-based security restrictions.

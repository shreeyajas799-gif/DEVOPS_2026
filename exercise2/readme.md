
# Exercise 2: Deploy Flask App on Kubernetes

## Objective
Deploy a Python Flask application on a local Kubernetes cluster using Minikube, Docker, and Kubernetes YAML files.

## Technologies Used
- Python and Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## Steps Performed
1. Started Minikube using Docker.
2. Created a Flask application (`app.py`).
3. Built the Docker image and loaded it into Minikube.
4. Created a Kubernetes Deployment and NodePort Service using `flask-deployment.yaml`.
5. Verified the Pod, Deployment, and Service.
6. Accessed the application using the Minikube Service URL.

## Commands
```bash
minikube start --driver=docker
docker build -t flask-app:latest .
minikube image load flask-app:latest
kubectl apply -f flask-deployment.yaml
kubectl get deployments
kubectl get pods
kubectl get services
minikube service flask-app-service --url
```

## Expected Output
```text
Hello from Flask on Kubernetes!
```

## Result
Successfully deployed and accessed a Flask application using Kubernetes on Minikube.

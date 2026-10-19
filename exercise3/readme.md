
# Exercise 3: Scaling Flask App using Kubernetes ReplicaSets

## Objective
Deploy a Flask-based flash sale application and learn how Kubernetes ReplicaSets maintain and scale Pods.

## Technologies Used
- Python and Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## Features
- `/` - Displays a welcome message and the serving Pod name.
- `/buy` - Simulates a purchase and identifies the serving Pod.
- `/health` - Checks application health.
- ReplicaSet - Maintains the desired number of Pods.
- NodePort Service - Exposes the application for testing.

## Steps Performed
1. Created the Flask application and Docker image.
2. Deployed three replicas using a Kubernetes ReplicaSet.
3. Scaled the ReplicaSet to five replicas.
4. Deleted a Pod and verified automatic replacement.
5. Accessed and tested the application through the Service.

## Commands
```bash
minikube start --driver=docker
docker build -t flashsale:1.0 .
minikube image load flashsale:1.0
kubectl apply -f flashsale-replicaset.yaml
kubectl get pods -l app=flashsale
kubectl scale rs flashsale-rs --replicas=5
kubectl get pods -l app=flashsale -o wide
minikube service flashsale-svc --url
```

## Result
Successfully deployed the Flask application, scaled it to five Pods, and verified ReplicaSet recovery after Pod deletion.

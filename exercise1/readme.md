
# Kubernetes Exercise 1: Hello Pod

## Overview
This exercise demonstrates how to deploy an Nginx web server on a local Kubernetes cluster using Minikube. The application simulates a simple Zepto storefront page and shows how Kubernetes runs and exposes containerized applications.

## Technologies Used
- Kubernetes
- Minikube
- Docker Desktop
- Nginx

## Steps Performed

### 1. Start Minikube
```bash
minikube start --driver=docker
```

### 2. Create the Nginx Pod
```bash
kubectl run hello-k8s --image=nginx --port=80
```

### 3. Verify the Pod
```bash
kubectl get pods
kubectl describe pod hello-k8s
kubectl logs hello-k8s
```

### 4. Expose the Pod Using a NodePort Service
```bash
kubectl expose pod hello-k8s --type=NodePort --port=80
```

### 5. Verify the Service and Open the Application
```bash
kubectl get services
minikube service hello-k8s
```

Minikube opens the Nginx welcome page in the browser. On macOS using the Docker driver, keep the terminal running while accessing the service.

## Screenshots

### Commands and Kubernetes Output
![Commands and Kubernetes Output](commands.png)

### Final Nginx Welcome Page
![Nginx Welcome Page](final_page.png)

## Result
- The `hello-k8s` Pod reached the `Running` state.
- A NodePort Service exposed the application on port 80.
- The Nginx welcome page opened successfully in the browser.

## Cleanup
To delete the resources created in this exercise:

```bash
kubectl delete service hello-k8s
kubectl delete pod hello-k8s
```

To stop Minikube:

```bash
minikube stop
```
